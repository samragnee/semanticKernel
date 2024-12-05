from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from dotenv import load_dotenv
import os

class ChatCompletionPlugin:
    def __init__(self):
        """
        Initializes the ChatCompletionPlugin by loading environment variables
        and setting up the OpenAI ChatCompletion service.
        """
        load_dotenv()  # Load environment variables from .env file
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.endpoint = os.getenv("OPENAI_API_ENDPOINT", "https://api.openai.com/v1")
        self.model_id = os.getenv("OPENAI_MODEL_ID", "gpt-4")

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

        # Initialize OpenAI ChatCompletion service
        self.chat_service = OpenAIChatCompletion(
            ai_model_id=self.model_id,
            api_key=self.api_key,
            endpoint=self.endpoint
        )

    def get_response(self, prompt, max_tokens=500, temperature=0.7):
        """
        Sends a user prompt to the OpenAI model and retrieves a response.

        Args:
            prompt (str): The user's input to the chatbot.
            max_tokens (int): The maximum number of tokens to include in the response.
            temperature (float): The randomness of the response.

        Returns:
            str: The response from the OpenAI model.
        """
        try:
            response = self.chat_service.complete(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.strip()
        except Exception as e:
            return f"An error occurred while processing the request: {e}"
