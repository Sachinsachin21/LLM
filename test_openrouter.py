import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

# Get API key
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

print(f"OpenRouter API Key present: {'Yes' if openrouter_api_key else 'No'}")
print(f"API Key starts with: {openrouter_api_key[:10]}..." if openrouter_api_key else "No key found")

if not openrouter_api_key:
    print("❌ OPENROUTER_API_KEY is missing!")
    exit(1)

# Test OpenRouter API
print("\nTesting OpenRouter API...")
try:
    llm = ChatOpenAI(
        model="moonshotai/kimi-dev-72b:free",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=openrouter_api_key
    )
    
    response = llm.invoke("Hello, this is a test message. Please respond with 'Test successful!'")
    print("✅ OpenRouter API is working!")
    print(f"Response: {response.content}")
    
except Exception as e:
    print(f"❌ OpenRouter API error: {e}")
    print(f"Error type: {type(e).__name__}")
    
    if "AuthenticationError" in str(e):
        print("\n🔧 Authentication Error Troubleshooting:")
        print("1. Check if your OpenRouter API key is correct")
        print("2. Make sure you have credits in your OpenRouter account")
        print("3. Verify your account is properly set up at https://openrouter.ai/")
        print("4. Try a different model if this one is not available")

print("\nOpenRouter API test complete!") 