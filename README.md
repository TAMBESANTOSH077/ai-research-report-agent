AI Research & Report Agent

An AI-powered research agent that takes a user's goal, creates an execution plan, selects appropriate tools, performs research/calculations, handles tool failures, and generates a structured final report.

Problem Statement

When a user wants information about a company or a topic, they normally need to search multiple sources, compare information, perform calculations, and prepare a report manually.

The goal of this project is to build an AI agent that can break a user's goal into smaller steps and execute those steps using appropriate tools.

For example:

"Research Tesla and give me a short report about the company and its products."

The agent plans the task, selects a research tool, collects information, and generates a report.

Main Goal

The main goal is to demonstrate an AI agent workflow:

User Goal
   ↓
Planning
   ↓
Tool Selection
   ↓
Tool Execution
   ↓
Result Evaluation
   ↓
Failure Recovery
   ↓
Final Report

The project focuses on agent decision-making, rather than simply generating an answer with an LLM.

Key Features
AI-based task planning
Tool selection
Company research
Calculator tool
Report generation
Failure detection
Recovery handling
Structured execution history
FastAPI backend
Simple web frontend
Gemini API integration


Architecture
                    USER
                     |
                     v
              Web Frontend
                     |
                     v
              FastAPI Backend
                     |
                     v
                AI Agent
                     |
             +-------+-------+
             |               |
             v               v
          Planner        Tool Selection
                             |
                 +-----------+-----------+
                 |           |             |
                 v           v             v
              Search     Calculator     Report
                 |           |             |
                 +-----------+-------------+
                             |
                             v
                       Tool Results
                             |
                             v
                     Result Evaluation
                             |
                      +------+------+
                      |             |
                    Useful      Failure
                      |             |
                      |         Recovery
                      |             |
                      +------+------+
                             |
                             v
                       Final Report
Agent Pipeline
1. User provides a goal

Example:

Research Tesla and give me a short report about the company and its products.
2. Agent creates a plan

Example:

1. Research Tesla's company information
2. Identify Tesla's main products
3. Organize the collected information
4. Generate a final report
3. Tool selection

The agent determines which tool is required.

Available tools:

search_company
calculator
report_generator
4. Tool execution

The selected tool performs the required operation.

5. Failure handling

If a tool fails, the agent records the failure and attempts the defined recovery path.

Example:

Search Tesla
     ↓
Success

or:

Search BYD
     ↓
Failure
     ↓
Record failure
     ↓
Continue / recover
6. Final report

The collected results are passed to the report-generation component.

Project Structure
agent-system/
│
├── app/
│   ├── main.py
│   │
│   ├── agent/
│   │   ├── agent.py
│   │   ├── planner.py
│   │   ├── state.py
│   │   └── recovery.py
│   │
│   ├── tools/
│   │   ├── search_tool.py
│   │   ├── calculator_tool.py
│   │   └── report_tool.py
│   │
│   └── services/
│       └── llm_service.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
Technology Stack
Backend
Python
FastAPI
Uvicorn
AI
Google Gemini API
Frontend
HTML
CSS
JavaScript
Development
Git
GitHub
Virtual Environment
Example
Input
Research Tesla and give me a short report about the company and its products.
Agent Plan
1. Research Tesla
2. Identify Tesla products
3. Organize research information
4. Generate final report
Execution
✓ Research Tesla
✓ Identify products
✓ Organize information
✓ Generate report
Output
AI Research Report


Goal:
Research Tesla and give me a short report about the company and its products.


Research Results:
...


Conclusion:
...
Failure Recovery

The project intentionally demonstrates what happens when a tool fails.

For example:

User Goal
   ↓
Agent Plan
   ↓
Search Company
   ↓
Search Failure
   ↓
Failure Recorded
   ↓
Recovery Logic
   ↓
Continue Execution

This is important because real AI agents cannot assume that every external tool will always work.

Why Use an Agent?

A normal LLM application can follow:

Question → LLM → Answer

This project uses:

Goal
 ↓
Plan
 ↓
Decide
 ↓
Use Tool
 ↓
Evaluate
 ↓
Recover
 ↓
Report

The agent therefore has a structured workflow for completing a task instead of simply generating a response.

API
Start the server
uvicorn app.main:app --reload

Application:

http://127.0.0.1:8000/

FastAPI documentation:

http://127.0.0.1:8000/docs
Environment Variables





Installation

Clone the repository:



Move into the project:



Create virtual environment:

python -m venv .venv

Activate on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run:

uvicorn app.main:app --reload
Example Use Cases

The agent can be used for goals such as:

Research Tesla and prepare a short report.
Research TCS and summarize the company.
Calculate the difference between two values.
Prepare a structured report from the collected information.

The system is designed so that additional tools can be added later without changing the entire agent architecture.

Advantages
1. Modular

Planning, tools, LLM services, and recovery are separated.

2. Extensible

New tools can be added easily.

For example:

Search Tool
Calculator
Report Generator
     +
Email Tool
Database Tool
Weather Tool
3. Automated

The agent can decide the execution flow based on the user's goal.

4. Failure Handling

Tool failures are recorded instead of silently ignored.

5. Reusable Architecture

The same architecture can be adapted to different agent-based applications.

Limitations
Company information is currently limited by the available search/data implementation.
Tool selection is partially rule-based in the current implementation.
Gemini API usage is subject to API quotas and limits.
The system is a demonstration project rather than a production research platform.
External tools can fail or return incomplete information.
Future Improvements

Possible improvements include:

Real web search integration
More intelligent tool selection
LangGraph-based workflow
Persistent agent state
More advanced recovery strategies
Multiple research sources
Source citations
Parallel tool execution
Human approval for sensitive actions
Long-term memory
Production monitoring
Key Learning

This project demonstrates how an AI agent can transform a high-level user goal into an executable workflow.

Goal
 ↓
Plan
 ↓
Choose
 ↓
Execute
 ↓
Evaluate
 ↓
Recover
 ↓
Report

The main idea is to move from a simple LLM question-answer system toward a more structured AI agent system capable of planning and using tools.

Conclusion

The AI Research & Report Agent demonstrates a modular approach to building an AI agent that can plan tasks, select tools, execute operations, handle failures, and produce a final report.
