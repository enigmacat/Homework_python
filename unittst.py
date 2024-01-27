import logging
import unittest

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


def is_triangle_exists(a, b, c):
    """
    Проверяет, можно ли построить треугольник с заданными сторонами.

    Аргументы:
        a (float) - длина стороны a
        b (float) - длина стороны b
        c (float) - длина стороны c

    Возвращает:
        True, если треугольник существует, иначе False

    Примеры:
    # Тест для проверки существования треугольника, когда сумма любых двух сторон больше третьей
    >>> is_triangle_exists(3, 4, 5)
    True

    # Тест для проверки существования треугольника, когда сумма любых двух сторон меньше третьей
    >>> is_triangle_exists(1, 2, 4)
    False

    # Тест для проверки существования треугольника, когда одна сторона больше суммы двух других
    >>> is_triangle_exists(1, 3, 4)
    False

    # Тест для проверки существования равностороннего треугольника
    >>> is_triangle_exists(1, 1, 1)
    True

    # Тест для проверки существования равнобедренного треугольника
    >>> is_triangle_exists(1, 1, 2)
    False

    # Тест для проверки существования разностороннего треугольника
    >>> is_triangle_exists(1, 2, 3)
    True
    """
    if a + b > c and a + c > b and b + c > a:
        logger.info("Треугольник существует")
        if a == b == c:
            logger.info("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            logger.info("Треугольник равнобедренный")
        else:
            logger.info("Треугольник разносторонний")
    else:
        logger.error("Треугольник не существует")

    return True


class TestIsTriangleExists(unittest.TestCase):
    def test_is_triangle_exists_1(self):
        self.assertTrue(is_triangle_exists(3, 4, 5))

    def test_is_triangle_exists_2(self):
        self.assertFalse(is_triangle_exists(1, 2, 4))

    def test_is_triangle_exists_3(self):
        self.assertFalse(is_triangle_exists(1, 3, 4))

    def test_is_triangle_exists_4(self):
        self.assertTrue(is_triangle_exists(1, 1, 1))

    def test_is_triangle_exists_5(self):
        self.assertFalse(is_triangle_exists(1, 1, 2))

    def test_is_triangle_exists_6(self):
        self.assertTrue(is_triangle_exists(1, 2, 3))


if __name__ == '__main__':
    unittest.main()
