from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
import aiohttp
import requests
import json


class SolaxSensor(SensorEntity):
    def __init__(self, coordinator, sensor_type, name):
        self.coordinator = coordinator
        self._sensor_type = sensor_type
        self._attr_name = name

    @property
    def state(self):
        return self.coordinator.data.get(self._sensor_type)

    async def async_update(self):
        await self.coordinator.async_request_refresh()

class SolaxDataCoordinator:
    def __init__(self, hass, host, password):
        self.hass = hass
        self.host = host
        self.password = password
        self.data = {}

    async def async_refresh(self):
        url = f"http://{self.host}"
        payload = {"optType": "ReadRealTimeData", "pwd": self.password}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=payload) as response:
                if response.status == 200:
                    raw_data = await response.json()
                    self.data = parse_data(raw_data.Data, raw_data.type)


def read_8_bit_unsigned(n):
    return n % 256


def read_16_bit_signed(n):
    if n < 32768:
        return n
    else:
        return n - 65536


def read_32_bit_unsigned(a, b):
    return b + 65536 * a


def read_32_bit_signed(a, b):
    if a < 32768:
        return b + 65536 * a
    else:
        return b + 65536 * a - 4294967296


def parse_data(data, inverter_type):
    # Parsing based on inverter type
    if inverter_type == 7:  # Example: parsing for inverter type 7
        return {
            "Yield_Today": data[21] / 10,
            "Yield_Total": read_32_bit_unsigned(data[19], data[20]) / 10,
            "PowerDc1": data[13],
            "PowerDc2": data[14],
            "feedInPower": read_32_bit_signed(data[74], data[75]),
            "GridAPower": read_16_bit_signed(data[6]),
            "GridBPower": read_16_bit_signed(data[7]),
            "GridCPower": read_16_bit_signed(data[8]),
            "FeedInEnergy": read_32_bit_unsigned(data[76], data[77]) / 100,
            "ConsumeEnergy": read_32_bit_unsigned(data[78], data[79]) / 100,
            "RunMode": data[18],
            "Vdc1": data[9] / 10,
            "Vdc2": data[10] / 10,
            "Idc1": data[11] / 10,
            "Idc2": data[12] / 10,
            "GridAVoltage": data[0] / 10,
            "GridBVoltage": data[1] / 10,
            "GridCVoltage": data[2] / 10,
            "GridACurrent": read_16_bit_signed(data[3]) / 10,
            "GridBCurrent": read_16_bit_signed(data[4]) / 10,
            "GridCCurrent": read_16_bit_signed(data[5]) / 10,
            "FreqacA": data[15] / 100,
            "FreqacB": data[16] / 100,
            "FreqacC": data[17] / 100,
            "BatteryCapacity": data[20],
            "BatteryVoltage": data[16] / 100,
            "BatteryTemperature": read_16_bit_signed(data[19]),
        }
    # Add parsing logic for other inverter types as needed
    return {}