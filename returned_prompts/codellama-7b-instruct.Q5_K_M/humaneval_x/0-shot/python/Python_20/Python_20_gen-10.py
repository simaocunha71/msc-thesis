from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    small = numbers[0]
    large = numbers[0]
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) < abs(numbers[i] - large):
            small = numbers[i - 1]
            large = numbers[i]
        elif abs(numbers[i] - numbers[i - 1]) == abs(numbers[i] - large):
            if numbers[i] < large:
                small = numbers[i - 1]
                large = numbers[i]
        elif abs(numbers[i] - numbers[i - 1]) > abs(numbers[i] - large):
            small = numbers[i]
            large = numbers[i - 1]
    return small, large


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_two(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_three(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.5]), (2.0, 4.5))


if __name__ == "__main__":
    unittest.main()
