weather_tool =  {
        "name": "get_weather",
        "type": "function",  # wymagane
        "description": "Check actual weather in the given city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            },
            "required": ["city"],
            "examples": [
                {"city": "Warszawa"},
                {"city": "Kraków"}
            ]
        }
    }

