import unittest


def calculator(numbers: str) -> int:
    result = 0
    delimiters = ","
    if numbers.startswith("//"):  # Check if custom delimiters is given
        delimiters, numbers = numbers[2:].split("\n")
        if len(delimiters) > 1:
            if "[" in delimiters:
                for x in delimiters.split("[")[1]:
                    numbers = numbers.replace(x[0], ",")
                delimiters = ","
            else:
                delimiters = delimiters[1]
    else:
        numbers = numbers.replace("\n", delimiters)  # Replace newline with delimiters
    numbers = numbers.strip(delimiters)  # Strip delimiterss
    if not numbers or numbers.isspace():
        return 0
    negatives = []
    all_numbers = numbers.split(delimiters)
    for number in all_numbers:
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
        self.assertEqual(calculator("5,4,6"), 15)

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

    def test_calculator_multiple_delimiters(self):
        self.assertEqual(calculator("//[;;;;]\n1;;2"), 3)

    def test_calculator_multiple_different_delimiter(self):
        self.assertEqual(calculator("//[;][,]\n1,2;3"), 6)

    def test_calculator_empty_str(self):
        self.assertEqual(calculator("    "), 0)


if __name__ == "__main__":
    unittest.main()
