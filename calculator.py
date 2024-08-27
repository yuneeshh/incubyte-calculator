import unittest


def calculator(numbers: str) -> int:
    result = 0
    delimiter = ","
    if numbers.startswith("//"):  # Check if custom delimiter is given
        delimiter = numbers[2]  # Get the delimiter
        numbers = numbers[3:]  # Slice after delimiter
    numbers = numbers.replace("\n", delimiter)  # Replace newline with delimiters
    if not numbers:
        return 0
    numbers = numbers.strip(delimiter)  # Strip delimiters
    negatives = []
    for number in numbers.split(delimiter):
        if number:
            if num := int(number):
                if num < 0:
                    negatives.append(number)
                    continue
                if num > 1000:
                    continue
                result += num
    if negatives:
        raise ValueError(f"Negative numbers not allowed {','.join(negatives)}")
    return result


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

    def test_calculator_delimiter(self):
        self.assertEqual(calculator("//;\n1;2"), 3)

    def test_calculator_multiple_delimiter(self):
        self.assertEqual(calculator(",1,,2"), 3)
        self.assertEqual(calculator("//;\n1;;2"), 3)

    def test_calculator_negative_digit(self):
        with self.assertRaises(ValueError) as cm:
            calculator("1,-2,3")
        self.assertEqual(str(cm.exception), "Negative numbers not allowed -2")

    def test_calculator_greater_1000(self):
        self.assertEqual(calculator("1000,2,1,1001"), 1003)

    def test_calculator_multiple_delimiter(self):
        self.assertEqual(calculator("//;;;;\n1;;2"), 3)


if __name__ == "__main__":
    unittest.main()
