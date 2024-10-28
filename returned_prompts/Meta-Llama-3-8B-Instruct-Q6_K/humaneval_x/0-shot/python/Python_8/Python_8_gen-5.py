from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if len(numbers) == 0:
        return 0, 1
    else:
        total_sum = sum(numbers)
        total_product = 1
        for num in numbers:
            total_product *= num
        return total_sum, total_product


if __name__ == "__main__":
    print(sum_product([]))  # (0, 1)
    print(sum_product([1, 2, 3, 4]))  # (10, 24)
    print(sum_product([-1, -2, -3, -4]))  # (-10, 24)
    print(sum_product([1, 2, 3, 4, 5]))  # (15, 120)
    print(sum_product([1, -2, 3, -4, 5]))  # (3, 60)  # 1 + -2 + 3 + -4 + 5 = 3, 1 * -2 * 3 * -4 * 5 = 60
    print(sum_product([-1, -2, -3, -4, -5]))  # (-15, 120)  # -1 + -2 + -3 + -4 + -5 = -15, 1 * -2 * -3 * -4 * -5 = 120
    print(sum_product([]))  # (0, 1)  # 0 = 0, 1 = 1
    print(sum_product([1]))  # (1, 1)  # 1 = 1, 1 = 1
    print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # (55, 3628800)  # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55, 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800
    print(sum_product([-1, 2, -3, 4, -5, 6]))  # (2, -120)  # -1 + 2 + -