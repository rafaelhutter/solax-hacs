# Solax Inverter Data Fetcher

This script connects to a Solax inverter over the local network to retrieve real-time performance data. It communicates with the inverter's API and displays key metrics in a structured format.

---

## How It Works

1. **Configuration**: 
   - When you run the script, it will prompt you to input the local IP address of your inverter and the corresponding API password.
2. **Data Retrieval**: 
   - The script sends a request to the inverter's local API endpoint to fetch data.
3. **Data Parsing**: 
   - The retrieved data is parsed and presented in a human-readable JSON format.

---

## Example Output

Here's an example of the JSON output:

```json
{
    "SN": "123456789",
    "Version": "2.031.01",
    "Inverter_Type": 7,
    "Parsed_Data": {
        "Yield_Today": 12.4,
        "Yield_Total": 3456.7,
        "PowerDc1": 500,
        "PowerDc2": 480,
        "feedInPower": 200,
        "BatteryCapacity": 90,
        "BatteryVoltage": 48.2,
        "GridAVoltage": 230.1,
        "FreqacA": 50.01,
        "ConsumeEnergy": 43.21
    }
}
