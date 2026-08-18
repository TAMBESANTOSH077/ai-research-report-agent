import os

from dotenv import load_dotenv
from google import genai


# --------------------------------
# LOAD ENVIRONMENT
# --------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env"
    )


client = genai.Client(
    api_key=api_key
)


MODEL = "gemini-2.5-flash"


# --------------------------------
# 1. CREATE PLAN
# --------------------------------

def generate_plan(goal: str):

    prompt = f"""
You are an AI research planning agent.

User Goal:
{goal}

Create a short practical plan to complete this goal.

Return ONLY a numbered list.

Do not perform the research.
Only create the plan.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()


# --------------------------------
# 2. GENERATE FINAL REPORT
# --------------------------------

def generate_report(
    goal: str,
    tool_results: list
):

    results_text = ""

    for result in tool_results:

        results_text += f"""
Tool: {result.get("tool", "Unknown")}

Result:
{result.get("result", "No result")}

"""

    prompt = f"""
You are an AI research report generator.

User Goal:
{goal}

Research results collected by the agent:

{results_text}

Create a short, clear and structured report.

Use ONLY the research results provided above.

Do not invent information.

Use this structure:

# AI Research Report

## Goal

## Findings

## Conclusion
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()