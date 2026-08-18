from app.services.llm_service import generate_plan


def create_plan(goal: str):

    plan_text = generate_plan(goal)

    steps = []

    for line in plan_text.splitlines():

        line = line.strip()

        if not line:
            continue

        # Remove numbering such as:
        # 1.
        # 2.
        # 3.
        if "." in line[:4]:
            line = line.split(".", 1)[1].strip()

        steps.append(line)

    return steps