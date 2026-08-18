from typing import Any


class AgentState:

    def __init__(self, goal: str):

        self.goal = goal

        self.plan = []

        self.completed_steps = []

        self.tool_results = []

        self.failures = []

        self.final_report = None

    def add_plan_step(self, step: str):

        self.plan.append(step)

    def add_completed_step(self, step: str):

        self.completed_steps.append(step)

    def add_tool_result(self, result: Any):

        self.tool_results.append(result)

    def add_failure(self, error: str):

        self.failures.append(error)

    def set_final_report(self, report: str):

        self.final_report = report

    def get_state(self):

        return {
            "goal": self.goal,
            "plan": self.plan,
            "completed_steps": self.completed_steps,
            "tool_results": self.tool_results,
            "failures": self.failures,
            "final_report": self.final_report
        }