"""Простой ипотечный калькулятор.

Содержит функции для расчёта ежемесячного платежа, общей суммы выплат
и переплаты по кредиту. При запуске как скрипт предоставляет
простейший CLI-интерфейс через input().
"""


def calculate_monthly_payment(
    principal: float,
    annual_rate_percent: float,
    years: int,
) -> float:
    """Рассчитать ежемесячный платёж по аннуитетной схеме.

    :param principal: сумма кредита (рубли), должна быть > 0
    :param annual_rate_percent: годовая ставка в процентах (например, 12.5)
    :param years: срок кредита в годах, должен быть > 0
    :return: ежемесячный платёж, округлён до двух знаков
    """
    if principal <= 0:
        raise ValueError("Сумма кредита должна быть положительной.")
    if years <= 0:
        raise ValueError("Срок кредита в годах должен быть положительным.")

    monthly_rate = annual_rate_percent / 100 / 12
    months = years * 12

    if monthly_rate == 0:
        return round(principal / months, 2)

    # Формула аннуитетного платежа
    factor = (1 + monthly_rate) ** months
    payment = principal * monthly_rate * factor / (factor - 1)
    return round(payment, 2)


def calculate_total_payment(monthly_payment: float, years: int) -> float:
    """Посчитать общую сумму выплат за весь срок кредита."""
    if monthly_payment < 0:
        raise ValueError("Ежемесячный платёж не может быть отрицательным.")
    if years <= 0:
        raise ValueError("Срок кредита в годах должен быть положительным.")

    months = years * 12
    return round(monthly_payment * months, 2)


def calculate_overpayment(principal: float, total_payment: float) -> float:
    """Посчитать переплату по кредиту (сумма процентов)."""
    if principal <= 0:
        raise ValueError("Сумма кредита должна быть положительной.")
    if total_payment < principal:
        raise ValueError("Общая выплата не может быть меньше суммы кредита.")

    return round(total_payment - principal, 2)


def run_cli() -> None:
    """Простой консольный интерфейс для демонстрации работы калькулятора."""
    print("Ипотечный калькулятор")
    //print("Это пример строки, которая будет слишком длинной и нарушит правила flake8, если длина строки превысит 88 символов")

    print("-" * 30)

    try:
        principal_str = input("Сумма кредита (руб): ")
        annual_rate_str = input("Годовая ставка (%): ")
        years_str = input("Срок (лет): ")

        principal = float(principal_str)
        annual_rate = float(annual_rate_str)
        years = int(years_str)

        monthly = calculate_monthly_payment(principal, annual_rate, years)
        total = calculate_total_payment(monthly, years)
        overpayment = calculate_overpayment(principal, total)

        print("\nРезультаты:")
        print(f"  Ежемесячный платёж: {monthly} руб.")
        print(f"  Общая сумма выплат: {total} руб.")
        print(f"  Переплата:          {overpayment} руб.")
    except ValueError as error:
        print(f"\nОшибка ввода: {error}")


if __name__ == "__main__":
    run_cli()
