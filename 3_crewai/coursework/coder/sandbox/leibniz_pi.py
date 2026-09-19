from decimal import Decimal, getcontext


def calculate_pi_terms(n_terms: int) -> Decimal:
    getcontext().prec = 50
    total = Decimal(0)
    sign = 1

    for i in range(n_terms):
        denominator = 2 * i + 1
        term = Decimal(sign) / Decimal(denominator)
        total += term
        sign *= -1

    return total * 4


if __name__ == "__main__":
    n = 1_000_000
    result = calculate_pi_terms(n)
    print(f"After {n} terms, 4 * (1 - 1/3 + 1/5 - 1/7 + ...) =")
    print(result)
