import unittest


def calculator(numbers: str) -> int:
    numbers = numbers.strip()
    return sum(int(number) for number in numbers.split())


class TestCalculator(unittest.TestCase):
    def test_calculator_empty_string(self):
        self.assertEqual(calculator(""), 0)

    def test_calculator_single_digit_string(self):
        self.assertEqual(calculator("5"), 5)


if __name__ == "__main__":
    unittest.main()
