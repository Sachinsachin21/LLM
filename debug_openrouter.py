import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

# Get API key
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

print(f"OpenRouter API Key present: {'Yes' if openrouter_api_key else 'No'}")
if openrouter_api_key:
    print(f"API Key starts with: {openrouter_api_key[:5]}...")
else:
    print("No key found")


if not openrouter_api_key:
    print("❌ OPENROUTER_API_KEY is missing from your .env file!")
    exit(1)

# Test OpenRouter API
print("\nTesting OpenRouter API with a direct call...")
try:
    llm = ChatOpenAI(
        model="moonshotai/kimi-dev-72b:free",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=openrouter_api_key
    )
    
    print("Attempting to invoke the model...")
    response = llm.invoke("Hello, this is a test message. Please respond with 'Test successful!'")
    print("✅ OpenRouter API is working!")
    print(f"Response: {response.content}")
    
except Exception as e:
    print(f"❌ OpenRouter API error: {e}")
    print(f"Error type: {type(e).__name__}")
    
    if "AuthenticationError" in str(e) or "BadRequestError" in str(e):
        print("\n🔧 Troubleshooting Steps:")
        print("1. Double-check your OPENROUTER_API_KEY in the .env file.")
        print("2. Ensure you have credits in your OpenRouter account: https://openrouter.ai/credits")
        print("3. Verify the model name 'moonshotai/kimi-dev-72b:free' is correct and available.")
        print("4. Check the OpenRouter status page for any ongoing incidents.")

print("\nOpenRouter API test complete!") 