from homeassistant import config_entries
from .const import DOMAIN, DEFAULT_NAME

class SolaxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({
                    vol.Required("host", default=''): str,
                    vol.Required("password", default=''): str
                })
            )
        return self.async_create_entry(title=DEFAULT_NAME, data=user_input)
