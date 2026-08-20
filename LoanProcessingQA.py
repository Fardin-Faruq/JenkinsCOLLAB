from LoanProcessingSystem import calculate_loan


def test_minimum_age():
    result = calculate_loan("C001", 18, 30000, 0, 750, "Salaried", 200000, 5)
    assert result["status"] == "Approved"
    print("Minimum age test: PASS")


def test_maximum_age():
    result = calculate_loan("C002", 65, 30000, 0, 750, "Salaried", 200000, 5)
    assert result["status"] == "Approved"
    print("Maximum age test: PASS")


def test_invalid_salary():
    try:
        calculate_loan("C003", 30, -1000, 0, 750, "Salaried", 200000, 5)
        print("Invalid salary test: FAIL")
    except ValueError:
        print("Invalid salary test: PASS")


def test_poor_credit_score():
    result = calculate_loan("C004", 30, 30000, 0, 500, "Salaried", 200000, 5)
    assert result["status"] == "Rejected"
    print("Poor credit score test: PASS")


def test_existing_loan_threshold():
    result = calculate_loan("C005", 30, 30000, 200000, 750, "Salaried", 100000, 5)
    assert result["status"] == "Rejected"
    print("Existing loan threshold test: PASS")


def test_high_dti():
    result = calculate_loan("C006", 30, 30000, 150000, 750, "Salaried", 100000, 5)
    assert result["status"] == "Rejected"
    print("High DTI test: PASS")


def test_employment_categories():
    salaried = calculate_loan("C007", 30, 30000, 0, 750, "Salaried", 200000, 5)
    self_employed = calculate_loan("C008", 30, 30000, 0, 750, "Self-Employed", 200000, 5)
    business = calculate_loan("C009", 30, 30000, 0, 750, "Business", 200000, 5)

    assert salaried["interest_rate"] == 7.5
    assert self_employed["interest_rate"] == 8.5
    assert business["interest_rate"] == 9.5

    print("Employment category test: PASS")


def test_boundary_loan_amount():
    result = calculate_loan("C010", 30, 30000, 0, 750, "Salaried", 10000, 5)
    assert result["status"] == "Approved"
    print("Boundary loan amount test: PASS")


def test_emi_calculation():
    result = calculate_loan("C011", 30, 30000, 0, 750, "Salaried", 200000, 5)

    rate = 7.5 / (12 * 100)
    months = 60

    expected_emi = 200000 * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)

    assert abs(result["emi"] - expected_emi) < 0.01
    print("EMI calculation test: PASS")


def test_invalid_input():
    try:
        calculate_loan("C012", 17, 30000, 0, 750, "Salaried", 200000, 5)
        print("Invalid input test: FAIL")
    except ValueError:
        print("Invalid input test: PASS")


def test_exception_handling():
    try:
        calculate_loan("C013", 30, 30000, 0, 750, "Unknown", 200000, 5)
        print("Exception handling test: FAIL")
    except ValueError:
        print("Exception handling test: PASS")


test_minimum_age()
test_maximum_age()
test_invalid_salary()
test_poor_credit_score()
test_existing_loan_threshold()
test_high_dti()
test_employment_categories()
test_boundary_loan_amount()
test_emi_calculation()
test_invalid_input()
test_exception_handling()
