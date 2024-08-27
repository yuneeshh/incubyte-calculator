import unittest


def calculator(numbers: str) -> int:
    numbers = numbers.strip()
    if not numbers:
        return 0
    return sum(int(number) for number in numbers.split(","))


class TestCalculator(unittest.TestCase):
    def test_calculator_empty_string(self):
        self.assertEqual(calculator(""), 0)

    def test_calculator_single_digit_string(self):
        self.assertEqual(calculator("5"), 5)

    def test_calculator_invalid_digit(self):
        with self.assertRaises(ValueError):
            calculator("a")

    def test_calculator_multiple_invalid_digit(self):
        with self.assertRaises(ValueError):
            calculator(",,k,,")

    def test_calculator_add_two_digit(self):
        self.assertEqual(calculator("5,4"), 9)

    def test_calculator_multiple_digits(self):
        self.assertEqual(calculator("5,4,6,7"), 22)

    def test_calculator_newline(self):
        self.assertEqual(calculator("1\n2,3"), 6)


if __name__ == "__main__":
    unittest.main()
