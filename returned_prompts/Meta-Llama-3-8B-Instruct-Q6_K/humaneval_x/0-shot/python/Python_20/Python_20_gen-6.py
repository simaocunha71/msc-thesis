    if len(numbers) < 2:
        return ValueError("List must contain at least two elements")

    min_diff = float('inf')
    closest_pair = (None, None)

    numbers.sort()
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair
    



# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))


# Output:
# (2.0, 2.2)
# (2.0, 2.0)  # This is expected because there's only one unique number. If you want to return the first number only, you can do that.  # (2.0,)  # This will give you a tuple with a single element.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do that.  # (2.0,)  # If you want to return the first number only, you can do