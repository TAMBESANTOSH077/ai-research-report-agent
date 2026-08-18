def calculate(expression: str):

    try:

        result = eval(
            expression,
            {
                "__builtins__": {}
            },
            {}
        )

        return result

    except Exception as error:

        raise Exception(
            f"Calculation failed: {error}"
        )