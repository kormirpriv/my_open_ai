from my_open_ai.functions.get_weather import get_weather
from my_open_ai.tools.weather_tool import weather_tool

TOOLS = [weather_tool]

TOOL_FUNCTIONS = {"get_weather": get_weather}
