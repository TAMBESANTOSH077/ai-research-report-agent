def generate_report(
    goal: str,
    research_results: list,
    calculations: list
):

    report = []

    report.append("# AI Research Report")

    report.append("\n## Goal")

    report.append(goal)

    report.append("\n## Research Results")

    for result in research_results:

        report.append(
            f"\n### {result.get('company', 'Unknown')}"
        )

        report.append(
            result.get(
                "description",
                "No information available."
            )
        )

    report.append("\n## Calculations")

    for calculation in calculations:

        report.append(
            f"""
Difference: {calculation.get('difference')}
Percentage Difference:
{calculation.get('percentage_difference')}%
"""
        )

    report.append("\n## Conclusion")

    report.append(
        "The report was generated using the agent's "
        "research and calculation tools."
    )

    return "\n".join(report)