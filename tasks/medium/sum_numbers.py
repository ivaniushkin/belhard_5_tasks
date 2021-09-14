"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет результат сложения цифр целого числа

ПРИМЕРЫ
--------------------------------------------------------------------------------
num_sum(5216) -> 14
num_sum(58716) -> 27
num_sum(321) -> 6
"""


def num_sum(numb: int) -> int:
    result = 0

    for i in str(numb):
        result += int(i)
    return result


if __name__ == '__main__':
    assert num_sum(5216) == 14
    print('Решено!')
