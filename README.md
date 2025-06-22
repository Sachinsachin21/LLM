# 🧠 CrewAI Agents with OpenRouter (LLM-Powered Research Tools)

This project demonstrates how to build intelligent agents using [CrewAI](https://github.com/joaomdmoura/crewai), [LangChain](https://www.langchain.com/), and [OpenRouter](https://openrouter.ai). It includes:

- 🔹 Single-agent demo for basic research tasks
- 🔹 Multi-agent simulation (Researcher + Writer)
- 🔹 OpenRouter API integration for LLM calls

---

## 📁 Project Files

| File                    | Description |
|-------------------------|-------------|
| `.env`                  | API keys for OpenRouter and optional services |
| `req.txt`               | Required Python packages |
| `Single_agent.py`       | Runs a simple single-agent LLM task |
| `Multi_agent.py`        | Launches a two-agent system for research + writing |
| `debug_openrouter.py`   | Debugs LLM responses from OpenRouter |
| `test_openrouter.py`    | Standalone OpenRouter model testing script |

---

## 🧰 Requirements

- Python 3.10+
- An OpenRouter API key (get one at [https://openrouter.ai](https://openrouter.ai))
- conda create -n agentdemo python=3.11 -y
- conda activate agentdemo
- pip install -r req.txt
=======
LLM

model = "moonshotai/kimi-dev-72b:free"
