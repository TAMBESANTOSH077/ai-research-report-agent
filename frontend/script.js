async function runAgent() {

    const goalInput =
        document.getElementById("goal");

    const runBtn =
        document.getElementById("runBtn");

    const status =
        document.getElementById("status");

    const goal =
        goalInput.value.trim();


    if (!goal) {

        status.textContent =
            "Please enter a goal.";

        status.className =
            "status error";

        return;
    }


    // --------------------------------
    // Reset UI
    // --------------------------------

    document.getElementById(
        "planSection"
    ).style.display = "none";

    document.getElementById(
        "executionSection"
    ).style.display = "none";

    document.getElementById(
        "failureSection"
    ).style.display = "none";

    document.getElementById(
        "reportSection"
    ).style.display = "none";


    runBtn.disabled = true;

    runBtn.textContent =
        "Agent Running...";


    status.textContent =
        "Agent is planning and executing tools...";

    status.className =
        "status loading";


    try {

        // --------------------------------
        // Call FastAPI backend
        // --------------------------------

        const response = await fetch(
            "/run-agent",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    goal: goal
                })
            }
        );


        const data =
            await response.json();


        console.log(
            "Agent response:",
            data
        );


        if (!response.ok || data.error) {

            throw new Error(
                data.error ||
                "Agent execution failed"
            );
        }


        // --------------------------------
        // STATUS
        // --------------------------------

        status.textContent =
            "Agent completed successfully.";

        status.className =
            "status success";


        // --------------------------------
        // PLAN
        // --------------------------------

        displayPlan(
            data.plan || []
        );


        // --------------------------------
        // EXECUTION
        // --------------------------------

        displayExecution(
            data
        );


        // --------------------------------
        // FAILURES
        // --------------------------------

        displayFailures(
            data.failures || []
        );


        // --------------------------------
        // REPORT
        // --------------------------------

        displayReport(
            data.report
        );


    } catch (error) {

        console.error(
            "Agent error:",
            error
        );


        status.textContent =
            "Error: " + error.message;

        status.className =
            "status error";


    } finally {

        runBtn.disabled = false;

        runBtn.textContent =
            "Run Agent";
    }
}


// --------------------------------
// DISPLAY PLAN
// --------------------------------

function displayPlan(plan) {

    const section =
        document.getElementById(
            "planSection"
        );

    const list =
        document.getElementById(
            "plan"
        );


    list.innerHTML = "";


    if (!plan.length) {

        list.innerHTML =
            "<li>No plan generated.</li>";

        section.style.display =
            "block";

        return;
    }


    plan.forEach(
        (step) => {

            const li =
                document.createElement(
                    "li"
                );

            li.textContent =
                step;

            list.appendChild(li);
        }
    );


    section.style.display =
        "block";
}


// --------------------------------
// DISPLAY EXECUTION
// --------------------------------

function displayExecution(data) {

    const section =
        document.getElementById(
            "executionSection"
        );

    const execution =
        document.getElementById(
            "execution"
        );


    execution.innerHTML = "";


    const completed =
        data.completed_steps || [];


    if (!completed.length) {

        execution.innerHTML =
            "<p>No completed steps.</p>";

    } else {

        completed.forEach(
            (step) => {

                const div =
                    document.createElement(
                        "div"
                    );

                div.className =
                    "execution-item";

                div.innerHTML = `
                    <span class="check">✓</span>
                    <span>${escapeHtml(step)}</span>
                `;

                execution.appendChild(
                    div
                );
            }
        );
    }


    section.style.display =
        "block";
}


// --------------------------------
// DISPLAY FAILURES
// --------------------------------

function displayFailures(failures) {

    const section =
        document.getElementById(
            "failureSection"
        );

    const container =
        document.getElementById(
            "failures"
        );


    container.innerHTML = "";


    if (!failures.length) {

        container.innerHTML =
            `<p class="no-failure">
                No failures detected.
            </p>`;

    } else {

        failures.forEach(
            (failure) => {

                const div =
                    document.createElement(
                        "div"
                    );

                div.className =
                    "failure-item";

                div.textContent =
                    failure;

                container.appendChild(
                    div
                );
            }
        );
    }


    section.style.display =
        "block";
}


// --------------------------------
// DISPLAY REPORT
// --------------------------------

function displayReport(report) {

    const section =
        document.getElementById(
            "reportSection"
        );

    const container =
        document.getElementById(
            "report"
        );


    if (!report) {

        container.textContent =
            "No final report generated.";

    } else {

        if (typeof report === "string") {

            container.textContent =
                report;

        } else {

            container.textContent =
                JSON.stringify(
                    report,
                    null,
                    2
                );
        }
    }


    section.style.display =
        "block";
}


// --------------------------------
// HTML SAFETY
// --------------------------------

function escapeHtml(text) {

    const div =
        document.createElement(
            "div"
        );

    div.textContent =
        text;

    return div.innerHTML;
}