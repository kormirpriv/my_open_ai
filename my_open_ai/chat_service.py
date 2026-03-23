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
                "content": "I'm pretty smart chatbot. "
                "You can use function or ask me about my opinion.",
            }
        ]

    def ask(self, user_input: str):
        self.messages.append({"role": "user", "content": user_input})
        max_call = 5
        call_left = max_call
        while call_left:

            response = client.responses.create(
                model="gpt-4.1-mini", input=self.messages, tools=TOOLS
            )
            tool_calls = [
                r
                for r in response.output
                if getattr(r, "type", None) in ["tool_call", "function_call"]
            ]
            if tool_calls:
                call_left -= 1
                for call in tool_calls:

                    if call.name not in TOOL_FUNCTIONS:
                        return f"Nieznane narzędzie: {call.name}"
                    tool_function = TOOL_FUNCTIONS[call.name]
                    try:
                        result = tool_function(**json.loads(call.arguments))
                    except TypeError as e:
                        logger.error(e)
                        return "Nie udało sie wywoałć narzędzia"

                    self.messages.append({"role": "assistant", "content": result})
                print(call_left)
                continue

            text = response.output_text

            if not text:
                text = "Nie udało się wygenerować odpowiedzi."

            self.messages.append({"role": "assistant", "content": text})
            return text

        return "Nie udało się uzyskać odpowiedzi po kilku próbach."
