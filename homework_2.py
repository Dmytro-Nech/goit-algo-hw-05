# Імпортуємо необхідні модулі
from typing import Callable
import re


def generator_numbers(text: str):
    # Очищуємо строку від всього окрім цифр
    list = re.findall(r"\d+\.\d+", text)
    # Створюємо генератор
    for n in list:
        yield float(n)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

def main():
    text = """Загальний дохід працівника складається з декількох частин: 
1000.01 як основний дохід, доповнений додатковими 
надходженнями 27.45 і 324.00 доларів."""
    total = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total}")

if __name__ == "__main__":
    main()