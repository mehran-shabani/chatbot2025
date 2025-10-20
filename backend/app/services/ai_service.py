
import openai
from app.config import settings

class AIService:
    def __init__(self):
        # API key is loaded from the central settings object
        self.api_key = settings.OPENAI_API_KEY
        if not self.api_key or self.api_key == "your_openai_api_key_here":
            raise ValueError("OPENAI_API_KEY is not configured in your environment or .env file.")
        openai.api_key = self.api_key

    def get_chat_completion(self, user_prompt: str, system_prompt: str = "You are a helpful assistant for researchers."):
        """
        Generates a chat completion using the OpenAI API.

        Args:
            user_prompt (str): The user's message.
            system_prompt (str): The system message to set the AI's behavior.

        Returns:
            A string containing the AI's response.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Or another suitable model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            # Basic error handling
            print(f"An error occurred with the OpenAI API: {e}")
            return "An error occurred while processing your request."

    def analyze_image_with_text(self, image_url: str, prompt: str):
        """
        Analyzes an image using a multi-modal model (like GPT-4 with Vision).
        NOTE: This is a placeholder for the actual implementation.

        Args:
            image_url (str): The URL of the image to analyze.
            prompt (str): The user's prompt related to the image.

        Returns:
            A string containing the AI's analysis.
        """
        # This function would use a model like gpt-4-vision-preview
        # The implementation details would involve sending a more complex
        # message structure with image URLs.
        print(f"Analyzing image: {image_url} with prompt: {prompt}")

        # Placeholder response
        return "Image analysis is a premium feature and is currently in development."

# Example usage (for demonstration)
if __name__ == '__main__':
    # This block requires the OPENAI_API_KEY to be set
    ai_service = AIService()

    # Test chat completion
    prompt = "Explain the significance of the Schrödinger equation in quantum mechanics."
    response = ai_service.get_chat_completion(prompt)

    print("AI Chat Response:")
    print(response)
