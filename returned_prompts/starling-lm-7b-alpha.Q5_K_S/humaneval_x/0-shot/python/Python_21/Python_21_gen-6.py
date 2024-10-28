def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    return [(x - min_num) / (max_num - min_num) for x in numbers]


# These "asserts" using `assert foreach_line` are just here for
# your sanity. They don't actually affect the correctness of the
# code. They're here to help you verify that your code is
# correctly grading your own tests, which can be useful
# when you're learning a new language or find yourself
# struggling with the subtlety of the correctness
# definitions.

def main():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert rescale_to_unit(numbers) == [0.0, 0.25, 0.5, 0.75, 1.0]
    numbers = [0.0, 0.0, 0.0, 0.0, 0.0]
    assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 0.0, 0.0]
    numbers = [0.0, 0.0, 0.0, 1.0, 1.0]
    assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 0.5, 0.5]
    numbers = [-5.0, -10.0, -1.0, 0.0, 1.0]
    assert rescale_to_unit(numbers) == [-0.5, -1.0, -0.25, 0.0, 0.25]
    print("All tests passed.")


if __name__ == "__main__":
    main()











































