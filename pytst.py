import logging
import pytest

# Импортируем библиотеку logging для логирования ошибок и полезной информации

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем файловый handler
file_handler = logging.FileHandler('log.txt')
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем handler в logger
logger.addHandler(file_handler)

# Ввод данных от пользователя
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

# Проверяем, можно ли построить треугольник с заданными сторонами


def is_triangle_exists(a, b, c):
    # Если сумма любых двух сторон больше третьей, то треугольник существует
    if a + b > c and a + c > b and b + c > a:
        logger.info("Треугольник существует")
        # Если все стороны равны, то треугольник равносторонний
        if a == b == c:
            logger.info("Треугольник равносторонний")
        # Если две стороны равны, то треугольник равнобедренный
        elif a == b or a == c or b == c:
            logger.info("Треугольник равнобедренный")
        # В противном случае, треугольник разносторонний
        else:
            logger.info("Треугольник разносторонний")
    # Если сумма любых двух сторон меньше третьей, то треугольник не существует
    else:
        logger.error("Треугольник не существует")


# Вызываем функцию is_triangle_exists с введенными данными
is_triangle_exists(a, b, c)


@pytest.mark.parametrize("a, b, c, expected", [
    # Тесты для проверки различных условий существования треугольника
    (3, 4, 5, True),
    (6, 7, 8, True),
    (1, 2, 3, True),
    (1, 2, 4, False),
    (1, 3, 4, False),
    (0, 0, 0, False),
    (1, 1, 1, True),
    (1, 1, 2, False),
    (1, 2, 3, True),
    (1, 2, 4, False),
    (1, 2, 5, True),
    (1, 2, 6, True),
    (1, 2, 7, True),
    (1, 2, 8, True),
    (1, 2, 9, True),
    (1, 2, 10, True),
])
def test_is_triangle_exists(a, b, c, expected):
    # Проверяем, что функция is_triangle_exists возвращает ожидаемое значение для различных комбинаций сторон треугольника
    assert is_triangle_exists(a, b, c) == expected
