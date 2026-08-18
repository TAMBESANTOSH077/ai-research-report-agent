def search_company(company: str):

    print(
        f"Searching information about {company}..."
    )

    company_key = company.strip().lower()


    # --------------------------------
    # Intentional failure
    # --------------------------------

    if company_key == "byd":

        raise Exception(
            "Simulated search service failure for BYD"
        )


    company_data = {

        "tcs": {

            "company":
                "Tata Consultancy Services (TCS)",

            "industry":
                "Information Technology Services",

            "description":
                "TCS is a global IT services and consulting company.",

            "services":
                "IT services, consulting, digital transformation, cloud, data and AI services"
        },


        "tesla": {

            "company":
                "Tesla",

            "industry":
                "Electric Vehicles and Clean Energy",

            "products":
                "Electric vehicles, energy storage systems and solar products"
        },


        "rivian": {

            "company":
                "Rivian",

            "industry":
                "Electric Vehicles",

            "products":
                "Electric trucks, SUVs and commercial vehicles"
        }

    }


    if company_key not in company_data:

        raise Exception(
            f"No information found for {company}"
        )


    return company_data[company_key]