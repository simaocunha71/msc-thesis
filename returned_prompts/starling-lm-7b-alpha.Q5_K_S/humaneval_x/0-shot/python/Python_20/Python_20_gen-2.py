def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_diff = float('inf')
    closest_pair = (None, None)
    for i in range(len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair


# These "asserts" using `assert()` are test cases.
# Run them to verify that this implementation actually passes all the test
# cases that come with the exercise, as well as the test cases you have added.
if __name__ == "__main__":
    import sys
    test_cases = sys.argv[1] if len(sys.argv) > 1 else ""
    test_cases = test_cases.split(",")
    for test_case in test_cases:
        try:
            func_name = test_case.split(":")[0]
            func = globals()[func_name] if func_name in globals() else None
            test_case_input, expect = test_case.split(":")[1].split(",")
            test_case_input = test_case_input.split(";")
            for i, input_ in enumerate(test_case_input):
                if func is None:
                    print(f"Function `{func_name}` not found.")
                else:
                    result = func(*input_.split())
                    if result != expect:
                        print(f"Got: `{result}`; Expected: `{expect}`")
        except Exception as e:
            print(f"Error: {e}")








# Here are some test cases to help you get started.
# You can add your own test cases as well.
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected: (2.0, 2.2