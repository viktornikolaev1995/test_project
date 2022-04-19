from warehouse_func import analyse
from promo_func import calculate


def test_anylyse():
    programm = [
        ('принять', 46, 'загрузить на вход'),
        ('выгрузить', 46),
        ('принять', 33, 'загрузить на вход'),
        ('принять', 555, 'загрузить на вход'),
        ('принять', 25, 'загрузить на вход'),
        ('принять', 55, 'загрузить на выход'),
        ('выгрузить', 25)
    ]
    assert analyse(programm) == 13
    programm = [
        ('принять', 55, 'загрузить на вход'),
        ('принять', 54, 'загрузить на вход'),
        ('принять', 53, 'загрузить на вход'),
        ('принять', 21, 'загрузить на выход'),
        ('принять', 26, 'загрузить на выход'),
        ('принять', 77, 'загрузить на вход'),
        ('принять', 78, 'загрузить на вход'),
        ('выгрузить', 78),
        ('выгрузить', 53)
    ]
    assert analyse(programm) == 29

    programm = [
        ('принять', 46, 'загрузить на вход'),
        ('выгрузить', 46),
        ('принять', 21, 'загрузить на выход'),
        ('выгрузить', 21)
    ]
    assert analyse(programm) == 4

    programm = [
        ('принять', 1, 'загрузить на выход'),
        ('принять', 2, 'загрузить на вход'),
        ('выгрузить', 1),
        ('принять', 3, 'загрузить на выход'),
        ('принять', 4, 'загрузить на вход'),
        ('выгрузить', 3),
    ]
    assert analyse(programm) == 6


def test_calculate():
    assert calculate(m=6, n=4, p=[1, 2, 4, 5]) == 12
    assert calculate(m=10, n=7, p=[10, 1, 2, 3, 4, 8, 7]) == 51
    assert calculate(m=3, n=3, p=[6, 2, 3]) == 12
    assert calculate(m=3, n=3, p=[2, 4, 8]) == 14