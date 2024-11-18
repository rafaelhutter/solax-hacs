from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class SolaxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Solax."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Validierung der Eingaben
            return self.async_create_entry(title="Solax", data=user_input)

        # Eingabemaske anzeigen
        data_schema = vol.Schema(
            {
                vol.Required("ip_address"): str,
                vol.Required("password"): str,
            }
        )
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
