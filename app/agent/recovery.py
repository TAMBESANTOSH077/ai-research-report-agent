import time


def execute_with_recovery(
    tool,
    argument,
    max_retries=2
):

    attempts = 0
    last_error = None

    while attempts <= max_retries:

        try:

            attempts += 1

            print(
                f"Tool attempt {attempts}/{max_retries + 1}"
            )

            result = tool(argument)

            return {
                "success": True,
                "result": result,
                "attempts": attempts,
                "error": None
            }

        except Exception as error:

            last_error = str(error)

            print(
                f"Tool failed: {last_error}"
            )

            if attempts <= max_retries:

                print(
                    "Recovery: retrying tool..."
                )

                time.sleep(1)

    return {
        "success": False,
        "result": None,
        "attempts": attempts,
        "error": last_error
    }