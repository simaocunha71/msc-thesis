def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest = numbers[0], numbers[1]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < abs(closest[0] - closest[1]):
                closest = numbers[i], numbers[j]
    return closest


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected: (2.0, 2.0)




def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest = numbers[0], numbers[1]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < abs(closest[0] - closest[1]):
                closest = numbers[i], numbers[j]
    return closest

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected: (2.0, 2.0)






def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest = min(numbers[:2]), min(numbers[1:])
    return closest

# Test cases
print