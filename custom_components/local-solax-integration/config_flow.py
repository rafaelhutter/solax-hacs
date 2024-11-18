import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD

class SolaxConfigFlow(config_entries.ConfigFlow, domain="solax_inverter"):
    """Handle the config flow for Solax Inverter."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Validate the inputs
            ip_address = user_input[CONF_IP_ADDRESS]
            password = user_input[CONF_PASSWORD]

            if not self._is_valid_ip_or_hostname(ip_address):
                errors["base"] = "invalid_ip"
            elif not password:
                errors["base"] = "invalid_password"
            else:
                # Proceed with setting up the configuration
                return self.async_create_entry(title="Solax Inverter", data=user_input)

        # Build the input form
        data_schema = vol.Schema(
            {
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Required(CONF_PASSWORD): str,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    def _is_valid_ip_or_hostname(self, value):
        """Validate if the value is a valid IP or hostname."""
        import ipaddress

        try:
            ipaddress.ip_address(value)  # Check if it's a valid IP
            return True
        except ValueError:
            # If not an IP, check if it's a valid hostname
            if len(value) > 255:
                return False
            if value[-1] == ".":
                value = value[:-1]  # Strip trailing dot for validation
            return all(
                part.isalnum() or part == "-"
                for part in value.split(".")
            )

        return False
