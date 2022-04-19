def calculate(m: int, n: int, p: list[int]) -> int:
    """словарь, где хранится текущее максимальное значение бонусов в случае, если участник участвует каждый день в
    промоакции"""
    results_for_case_1 = {
        'max_points': 0,
        'ach_level': None,
        'spent_days': []
    }
    """словарь, где хранится текущее максимальное значение бонусов, в случае, если участник пропускает один день в 
    промоакции, после нажатия на кнопку в случае, если количество бонусов для первого уровня превышает среднее значение 
    и это является лучшим исходом"""
    results_for_case_2 = {
        'max_points': 0,
        'ach_level': None,
        'spent_days': []
    }
    # 1 case
    for day, level in zip(range(1, m+1), range(1, n+1)):
        results_for_case_1['max_points'] = results_for_case_1['max_points'] + p[level - 1] \
            if results_for_case_1['max_points'] else p[level - 1]
        results_for_case_1['ach_level'] = level
        results_for_case_1['spent_days'].append(day)
    # 2 case
    average_value_of_list_of_bonuses = sum(p)/ len(p)  # среднее значение бонусов
    levels = [level for level in range(1, n+1)]  # количество уровней в промоакции
    days = [day for day in range(1, m+1, 2)]  # количество дней через один, при которых промоакция действительна

    """если значение бонуса в первый день превышает среднее значение бонусов в промоакции, то возможен вариант лучшего 
    исхода, т.е. большего количества полученных бонусов"""
    if p[0] >= average_value_of_list_of_bonuses:
        for day in days:
            results_for_case_2['max_points'] = results_for_case_2['max_points'] + p[0] \
                if results_for_case_1['max_points'] else p[0]
            results_for_case_2['ach_level'] = levels[0]
            results_for_case_2['spent_days'].append(day)
        if not m % 2:
            results_for_case_2['max_points'] += p[1]
            results_for_case_2['ach_level'] = levels[1]
            results_for_case_2['spent_days'].append(m)

    return results_for_case_1['max_points'] if results_for_case_1['max_points'] > results_for_case_2['max_points'] \
        else results_for_case_2['max_points']