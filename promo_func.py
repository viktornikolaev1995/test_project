def calculate(m: int, n: int, p: list[int]) -> int:
    current_day = 0  # текущий день
    current_level = 0  # текущий уровень
    bonuses = 0  # количество бонусов
    while current_level != n or current_day != m:
        print(current_level)
        print(current_day)
        current_day += 1
        current_level += 1
        bonuses += p[current_level - 1]

    print(bonuses)
    return bonuses

calculate(m=3, n=2, p=[6, 2, 3])