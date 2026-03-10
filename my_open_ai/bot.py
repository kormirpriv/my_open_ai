import json

from openai import OpenAI

from my_open_ai.config import config
from my_open_ai.functions.get_weather import get_weather
from my_open_ai.tools.weather_tool import weather_tool

client = OpenAI(api_key=config.openai_api_key)

messages = [
    {
        "role": "system",
        "content": "I'm pretty smart chatbot. You can use function or ask me about my opinion.",
    }
]

while True:
    user_input = input("👤 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("See you later!")
        break
    messages.append({"role": "user", "content": user_input})
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages,
        tools=weather_tool
    )
    output = response.output[0]
    print(output)
    if hasattr(output, "type") and output.type in ["tool_call", "function_call"]:
        print(output.name)
        tool_name = output.name
        arguments = json.loads(output.arguments)

        if tool_name == "get_weather":
            result = get_weather(**arguments)

        messages.append({
            "role": "assistant",
            "content": result
        })
        print(f"🤖 Bot: {result}")
        # followup = client.responses.create(
        #     model="gpt-4.1-mini",
        #     input=messages
        # )

        # final_text = followup.output_text
        # print(f"🤖 Bot: {final_text}")
        # messages.append({"role": "assistant", "content": final_text})

    else:
        text = response.output_text
        print(f"🤖 Bot: {text}")
        messages.append({"role": "assistant", "content": text})