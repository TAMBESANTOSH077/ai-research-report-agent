from app.agent.planner import create_plan

from app.services.llm_service import generate_report

from app.tools.search_tool import search_company
from app.tools.calculator_tool import calculate


# --------------------------------
# LOCAL TOOL SELECTION
# --------------------------------

def select_tool_locally(goal: str):

    text = goal.lower()

    calculation_words = [
        "calculate",
        "difference",
        "sum",
        "subtract",
        "multiply",
        "divide",
        "percentage"
    ]

    for word in calculation_words:

        if word in text:
            return "calculator"


    research_words = [
        "research",
        "company",
        "about",
        "information",
        "report"
    ]

    for word in research_words:

        if word in text:
            return "search_company"


    return "search_company"


# --------------------------------
# EXTRACT COMPANY
# --------------------------------

def extract_company(goal: str):

    text = goal.lower()

    companies = {

        "tata consultancy services": "TCS",
        "tcs": "TCS",

        "tesla": "Tesla",

        "rivian": "Rivian",

        "byd": "BYD"
    }

    for key, company in companies.items():

        if key in text:
            return company

    return None


# --------------------------------
# CONVERT PLAN TO LIST
# --------------------------------

def normalize_plan(plan_text):

    # Gemini/planner returned a list
    if isinstance(plan_text, list):

        return [
            str(step).strip()
            for step in plan_text
            if str(step).strip()
        ]


    # Gemini/planner returned a string
    if isinstance(plan_text, str):

        plan = []

        for line in plan_text.splitlines():

            line = line.strip()

            if not line:
                continue

            # Remove numbering
            if "." in line[:4]:

                cleaned = line.split(
                    ".",
                    1
                )[1].strip()

            else:

                cleaned = line

            if cleaned:
                plan.append(cleaned)

        return plan


    # Unexpected format
    return []


# --------------------------------
# RUN AGENT
# --------------------------------

def run_agent(goal: str):

    print("\n==============================")
    print("AGENT STARTED")
    print("==============================")

    print("\nGOAL:")
    print(goal)


    # --------------------------------
    # 1. CREATE PLAN
    # Gemini Call #1
    # --------------------------------

    print("\nCreating plan...")

    plan_text = create_plan(goal)

    print("\nRAW PLAN:")
    print(plan_text)


    # Convert list/string safely
    plan = normalize_plan(plan_text)

    print("\nNORMALIZED PLAN:")

    for step in plan:

        print(
            f"- {step}"
        )


    # --------------------------------
    # 2. LOCAL TOOL SELECTION
    # No Gemini call
    # --------------------------------

    selected_tool = select_tool_locally(
        goal
    )

    print(
        "\nSelected tool:",
        selected_tool
    )


    tool_results = []

    completed_steps = []

    failures = []


    # --------------------------------
    # 3. EXECUTE SEARCH TOOL
    # --------------------------------

    if selected_tool == "search_company":

        company = extract_company(
            goal
        )


        if not company:

            failures.append(
                "Could not identify a company from the goal."
            )


        else:

            print(
                f"\nSearching company: {company}"
            )

            try:

                result = search_company(
                    company
                )


                tool_results.append({

                    "tool": "search_company",

                    "result": result

                })


                completed_steps.append(
                    f"Research information about {company}"
                )


                print(
                    "\nSearch successful."
                )


            except Exception as error:

                print(
                    "\nSearch failed:",
                    error
                )


                failures.append(
                    f"Search failed: {company}"
                )


    # --------------------------------
    # 4. EXECUTE CALCULATOR
    # --------------------------------

    elif selected_tool == "calculator":

        try:

            result = calculate(
                goal
            )


            tool_results.append({

                "tool": "calculator",

                "result": result

            })


            completed_steps.append(
                "Performed requested calculation"
            )


        except Exception as error:

            print(
                "\nCalculator failed:",
                error
            )


            failures.append(
                "Calculator failed"
            )


    # --------------------------------
    # 5. GENERATE FINAL REPORT
    # Gemini Call #2
    # --------------------------------

    print(
        "\nGenerating final report..."
    )


    try:

        report = generate_report(
            goal,
            tool_results
        )


        completed_steps.append(
            "Generated final report"
        )


    except Exception as error:

        print(
            "\nReport generation failed:",
            error
        )


        failures.append(
            "Report generation failed"
        )


        report = (
            "Unable to generate the final report."
        )


    # --------------------------------
    # 6. FINAL RESPONSE
    # --------------------------------

    print("\n==============================")
    print("AGENT FINISHED")
    print("==============================")


    return {

        "goal": goal,

        "plan": plan,

        "completed_steps":
            completed_steps,

        "failures":
            failures,

        "report":
            report
    }