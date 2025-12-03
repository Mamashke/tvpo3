"""Тесты для ипотечного калькулятора."""

import pytest

from mortgage_app import (
    calculate_monthly_payment,
    calculate_total_payment,
    calculate_overpayment,
)


def test_zero_interest_monthly_payment() -> None:
    """Без процентов: просто делим сумму на количество месяцев."""
    payment = calculate_monthly_payment(120_000, 0, 10)  # 10 лет = 120 месяцев
    assert payment == 1000.0


def test_normal_case_monthly_payment() -> None:
    """Обычный кредит: проверяем порядок величины ежемесячного платежа."""
    payment = calculate_monthly_payment(1_000_000, 10, 20)
    # Значение около 9650, допускаем 5% погрешности
    assert payment == pytest.approx(9650, rel=0.05)


def test_invalid_principal_for_monthly_payment() -> None:
    """Сумма кредита должна быть > 0."""
    with pytest.raises(ValueError):
        calculate_monthly_payment(0, 10, 10)


def test_invalid_years_for_monthly_payment() -> None:
    """Срок кредита в годах должен быть > 0."""
    with pytest.raises(ValueError):
        calculate_monthly_payment(1_000_000, 10, 0)


def test_total_payment_and_overpayment_consistency() -> None:
    """Общая сумма выплат должна быть больше суммы кредита при ненулевой ставке."""
    principal = 500_000
    years = 15
    annual_rate = 8.0

    monthly = calculate_monthly_payment(principal, annual_rate, years)
    total = calculate_total_payment(monthly, years)
    overpayment = calculate_overpayment(principal, total)

    assert total > principal
    assert overpayment == pytest.approx(total - principal, rel=1e-5)


def test_overpayment_raises_when_total_less_than_principal() -> None:
    """Если общая выплата меньше суммы кредита, должна быть ошибка."""
    """bebra"""
    with pytest.raises(ValueError):
        calculate_overpayment(100_000, 50_000)
