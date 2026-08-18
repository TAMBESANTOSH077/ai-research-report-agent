from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.agent.agent import run_agent


app = FastAPI(
    title="AI Research & Report Agent",
    description="Autonomous AI agent with planning, tool selection and recovery",
    version="1.0.0"
)


class AgentRequest(BaseModel):
    goal: str


# --------------------------------
# HEALTH
# --------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "message": "AI Agent API is running"
    }


# --------------------------------
# RUN AGENT
# --------------------------------

@app.post("/run-agent")
def run_agent_api(request: AgentRequest):

    if not request.goal.strip():

        return {
            "error": "Goal cannot be empty"
        }

    try:

        result = run_agent(
            request.goal
        )

        return result

    except Exception as error:

        print(
            "AGENT ERROR:",
            error
        )

        return {
            "error": str(error)
        }


# --------------------------------
# FRONTEND
# --------------------------------

FRONTEND_DIR = Path(__file__).resolve().parents[1] / "frontend"

app.mount(
    "/",
    StaticFiles(
        directory=FRONTEND_DIR,
        html=True
    ),
    name="frontend"
)