AI Research & Report Agent

An AI-powered research agent that takes a user's goal, creates a plan, selects the appropriate tool, executes the task, handles failures, and generates a structured final report.

Problem Statement

When a user wants to research a company or compare information, they normally need to manually:

Search for information.
Decide what information is relevant.
Perform calculations if required.
Organize the findings.
Create a final report.

The goal of this project is to automate this workflow using an AI agent with planning and tool selection.

Main Goal

The main goal is to build an agent that can take a natural-language goal and decide what steps and tools are required to complete it.

Example:

User:
Research Tesla and give me a short report about the company and its products.


        ↓


AI Agent


        ↓


Create Plan
        ↓
Select Tool
        ↓
Search Company
        ↓
Collect Results
        ↓
Generate Report
What I Built

The system contains:

AI-based planning
Tool selection
Company research
Calculator tool
Report generation
Failure handling
Simple web interface
FastAPI backend
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
          +--------+--------+
          |                 |
          v                 v
       Planner          Tool Selection
                            |
                 +----------+----------+
                 |          |           |
                 v          v           v
              Search    Calculator   Report
                 |          |           |
                 +----------+-----------+
                            |
                            v
                       Tool Results
                            |
                            v
                       Final Report
Agent Pipeline
User Goal
   ↓
Create Plan
   ↓
Understand Required Task
   ↓
Select Tool
   ↓
Execute Tool
   ↓
Check Result
   ↓
Handle Failure
   ↓
Generate Final Report
Example
Input
Research TCS and give me a short report.
Agent Plan
1. Research TCS company information
2. Collect relevant information
3. Organize the findings
4. Generate a short report
Tool Selection
search_company
Final Output
AI Research Report


Goal:
Research TCS and give me a short report.


Research Results:
TCS is a technology services and consulting company.


Products / Services:
- IT services
- Consulting
- Digital solutions


Conclusion:
TCS is a major technology services company.
Tools
1. Search Company

Used when the agent needs company information.

Example:

search_company("Tesla")
2. Calculator

Used when the user's goal requires numerical calculations.

Example:

Calculate the difference between 500 and 350.

The agent can select:

calculator
3. Report Generator

Used after collecting information.

It converts the tool results into a structured report.

Failure Recovery

The system also demonstrates failure handling.

For example, if a company search fails:

Search
   ↓
Failure
   ↓
Record failure
   ↓
Continue safely
   ↓
Generate available result

Example:

Search failed: BYD

Instead of crashing the complete application, the agent records the failure.

Technology Stack
Python
FastAPI
Google Gemini API
HTML
CSS
JavaScript
Uvicorn
python-dotenv
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
Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/ai-research-report-agent.git

Go into the project:

cd ai-research-report-agent

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a .env file locally:

GEMINI_API_KEY=your_api_key_here

Do not upload .env to GitHub.

Only upload:

.env.example

Example:

GEMINI_API_KEY=your_api_key_here
Run the Application

Start the FastAPI server:

uvicorn app.main:app --reload

Open the application:

http://127.0.0.1:8000/

FastAPI documentation:

http://127.0.0.1:8000/docs
Test Examples
Test 1 — Company Research
Research Tesla and give me a short report.

Expected:

Plan
↓
Search Tesla
↓
Generate Report
Test 2 — TCS
Research TCS and give me a report.

Expected:

Plan
↓
Identify TCS
↓
Search
↓
Generate Report
Test 3 — Calculation
Calculate the difference between 500 and 350.

Expected:

Calculator
↓
150
Test 4 — Failure
Research BYD and give me a report.

If the search tool fails, the agent records the failure instead of silently pretending that the information was retrieved.

Why I Built This

The main idea is to move from a simple chatbot to an agent that can decide how to solve a task.

A normal chatbot mainly does:

Question
   ↓
Answer

This project does:

Goal
 ↓
Plan
 ↓
Tool Selection
 ↓
Tool Execution
 ↓
Failure Handling
 ↓
Report

This makes the system more suitable for tasks where multiple steps and tools are required.

Advantages
Reduces manual research work.
Breaks complex goals into smaller steps.
Uses different tools for different tasks.
Can handle tool failures.
Produces a structured final report.
Modular design makes new tools easier to add.
Limitations

The current project is a demonstration rather than a full production research platform.

The company search tool currently uses a limited set of company data, so it does not provide unrestricted real-time web research.

The system also depends on the availability and quota of the Gemini API.

Future Improvements

Possible improvements include:

Real web search
More research tools
Multiple sources
Source citations
Vector database
Long-term agent memory
Better planning
Parallel tool execution
More advanced recovery strategies
Production authentication
Persistent execution history
Key Learning

The main learning from this project is that an AI agent is not simply an LLM generating an answer.

An agent can:

Understand the goal
      ↓
Plan the task
      ↓
Choose a tool
      ↓
Execute the tool
      ↓
Handle failure
      ↓
Use the result
      ↓
Produce the final answer

This project demonstrates that basic agent architecture using a practical research-and-report use case.