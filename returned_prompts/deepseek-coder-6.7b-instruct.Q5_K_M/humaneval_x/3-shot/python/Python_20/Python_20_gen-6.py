    numbers.sort()
    smallest_difference  _  float('inf')
    closest_pair  _  None

    for idx  _  range(len(numbers)  _  2):
        difference  _  numbers[idx + 1]  _  numbers[idx]

        if difference  <  smallest_difference:
            smallest_difference  _  difference
            closest_pair  _  (numbers[idx], numbers[idx + 1])

    return closest_pair


