    min_diff = float('inf')
    closest_pair = (None, None)

    for idx, num in enumerate(numbers):
        for idx2, num2 in enumerate(numbers):
            if idx != idx2:
                diff = abs(num - num2)
                if diff < min_diff:
                    min_diff = diff
                    closest_pair = (min(num, num2), max(num, num2))

    return closest_pair
# test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0) 
# test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0) 
# test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)  # test cases
# test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)  # test cases
# test cases
print(find_closest_elements([1.0, 2.0, 