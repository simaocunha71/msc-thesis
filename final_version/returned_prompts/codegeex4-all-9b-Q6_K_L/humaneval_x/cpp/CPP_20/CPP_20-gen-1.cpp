def find_closest_elements(numbers):
    if len(numbers) < 2:
        return None
    min_diff = float('inf')
    result = ()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                result = (numbers[i], numbers[j])
    return result

