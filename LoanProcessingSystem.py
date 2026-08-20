def calculate_loan(customer_id, age, salary, existing_loan, credit_score,
                   employment_type, requested_loan, tenure):

    if age < 18 or age > 65:
        raise ValueError("Invalid age")

    if salary <= 0:
        raise ValueError("Invalid salary")

    if existing_loan < 0:
        raise ValueError("Invalid existing loan amount")

    if credit_score < 300 or credit_score > 900:
        raise ValueError("Invalid credit score")

    if requested_loan <= 0:
        raise ValueError("Invalid loan amount")

    if tenure <= 0:
        raise ValueError("Invalid loan tenure")

    employment = employment_type.lower()

    if employment == "salaried":
        multiplier = 20
        interest_rate = 8.5
    elif employment == "self-employed":
        multiplier = 15
        interest_rate = 9.5
    elif employment == "business":
        multiplier = 12
        interest_rate = 10.5
    else:
        raise ValueError("Invalid employment type")

    debt_to_income = (existing_loan / (salary * 12)) * 100
    eligible_loan = salary * multiplier

    if credit_score >= 750:
        interest_rate -= 1
    elif credit_score < 600:
        interest_rate += 2

    if requested_loan < 10000 or requested_loan > eligible_loan:
        status = "Rejected"
    elif credit_score < 600:
        status = "Rejected"
    elif debt_to_income > 40:
        status = "Rejected"
    elif existing_loan > salary * 6:
        status = "Rejected"
    else:
        status = "Approved"

    monthly_rate = interest_rate / (12 * 100)
    months = tenure * 12

    emi = requested_loan * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

    return {
        "customer_id": customer_id,
        "debt_to_income": debt_to_income,
        "eligible_loan": eligible_loan,
        "interest_rate": interest_rate,
        "emi": emi,
        "status": status
    }


if __name__ == "__main__":
    try:
        customer_id = input("Enter Customer ID: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Monthly Salary: "))
        existing_loan = float(input("Enter Existing Loan Amount: "))
        credit_score = int(input("Enter Credit Score: "))
        employment_type = input("Enter Employment Type: ")
        requested_loan = float(input("Enter Requested Loan Amount: "))
        tenure = int(input("Enter Loan Tenure: "))

        result = calculate_loan(
            customer_id,
            age,
            salary,
            existing_loan,
            credit_score,
            employment_type,
            requested_loan,
            tenure
        )

        print("\nCustomer ID:", result["customer_id"])
        print("Debt-to-Income Ratio: {:.2f}%".format(result["debt_to_income"]))
        print("Eligible Loan Amount: {:.2f}".format(result["eligible_loan"]))
        print("Interest Rate: {:.2f}%".format(result["interest_rate"]))
        print("EMI: {:.2f}".format(result["emi"]))
        print("Loan Status:", result["status"])

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected Error:", e)
