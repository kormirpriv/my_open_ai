import json
import logging

from my_open_ai.logging_config import setup_logging
from my_open_ai.openai_client import client
from my_open_ai.tools.tool_registry import TOOL_FUNCTIONS, TOOLS

setup_logging()
logger = logging.getLogger(__name__)
class ChatService:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "I'm pretty smart chatbot. You can use function or ask me about my opinion.",
            }
        ]

    def ask(self, user_input: str):
        self.messages.append({"role": "user", "content": user_input})

        # 🔹 for loop tool calls (max 5)
        for _ in range(5):

            response = client.responses.create(
                model="gpt-4.1-mini", input=self.messages, tools=TOOLS
            )
            output = response.output[0]
            if hasattr(output, "type") and output.type in [
                "tool_call",
                "function_call",
            ]:
                tool_name = output.name
                arguments = json.loads(output.arguments)
                if tool_name not in TOOL_FUNCTIONS:
                    return f"Nieznane narzędzie: {tool_name}"
                tool_function = TOOL_FUNCTIONS[tool_name]
                try:
                    result = tool_function(**arguments)
                except TypeError as e:
                    logger.error(e)
                    return "Nie udało sie wywoałć narzędzia"


                self.messages.append({"role": "assistant", "content": result})

                continue

            text = response.output_text

            if not text:
                text = "Nie udało się wygenerować odpowiedzi."

            self.messages.append({"role": "assistant", "content": text})
            return text

        return "Nie udało się uzyskać odpowiedzi po kilku próbach."
