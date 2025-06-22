import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

OpenRouter_API = os.getenv("OPENROUTER_API_KEY")

if not OpenRouter_API:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables.")

def create_minimal_agent():
    llm = ChatOpenAI(
        model="moonshotai/kimi-dev-72b:free",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=OpenRouter_API,
        temperature=0.7,
        max_tokens=1000
    )
    
    return Agent(
        role="Simple Research Agent",
        goal="Provide a brief summary about AI in healthcare",
        backstory="You are a helpful AI assistant that provides concise information.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_simple_task(agent):
    return Task(
        description="Write a short paragraph about the latest developments in AI for healthcare.",
        agent=agent,
        expected_output="A brief summary of AI healthcare developments."
    )

if __name__ == "__main__":
    print("Testing minimal CrewAI agent with MoonshotAI model...")
    
    try:
        agent = create_minimal_agent()
        task = create_simple_task(agent)
        crew = Crew(agents=[agent], tasks=[task])
        
        result = crew.kickoff()
        print("\n✅ Success! Agent response:")
        print(result)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc() 