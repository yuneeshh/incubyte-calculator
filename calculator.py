import unittest


def calculator(numbers: str) ->int:
    return 0


class TestCalculator(unittest.TestCase):

    def test_add_empty(self):
        self.assertEqual(calculator(""), 0)


if __name__ == '__main__':
    unittest.main()
