import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

OpenRouter_API = os.getenv("OPENROUTER_API_KEY")

if not OpenRouter_API:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables.")

# Shared LLM for both agents
llm = ChatOpenAI(
    model="moonshotai/kimi-dev-72b:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=OpenRouter_API,
    temperature=0.7,
    max_tokens=2000
)

def run_researcher(topic):
    print("\n--- 👨‍🔬 Researcher Agent ---")
    system_prompt = "You are a research analyst. Your goal is to uncover cutting-edge developments in AI."
    human_prompt = f"Please conduct a comprehensive analysis of the latest advancements in {topic}. " \
                   "Your final answer must be a full analysis report."
    
    print("Generating research report...")
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ])
    print("--- ✅ Researcher Finished ---")
    return response.content

def run_writer(research_report, topic):
    print("\n--- ✍️ Writer Agent ---")
    system_prompt = "You are a content strategist. Your goal is to craft compelling content on AI."
    human_prompt = f"Using the following research report, compose an insightful article on {topic}. " \
                   "Your final answer must be the full blog post of at least 3 paragraphs.\n\n" \
                   f"Research Report:\n---\n{research_report}"

    print("Generating final article...")
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ])
    print("--- ✅ Writer Finished ---")
    return response.content


if __name__ == "__main__":
    print("🚀 Starting multi-agent simulation...")
    print(f"Using Model: {llm.model_name}")
    topic = ""
    try:
        topic = input("Enter the topic you want to research: ")
        if not topic.strip():
            topic = "AI in healthcare"
    except EOFError:
        topic = "AI in healthcare"
    
    print(f"\n🔬 Researching: {topic}")
    print("="*50)
    
    try:
        research_report = run_researcher(topic)
        print("\nResearch Report:\n", research_report)
        print("\n" + "="*50)
        
        final_article = run_writer(research_report, topic)
        
        print("\n✅ Simulation complete!")
        print("="*50)
        print("\nFinal Article:\n")
        print(final_article)

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc() 