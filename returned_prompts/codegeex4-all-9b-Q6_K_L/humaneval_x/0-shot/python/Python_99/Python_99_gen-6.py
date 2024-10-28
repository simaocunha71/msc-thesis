def closest_integer(value):
    # Convert the input to a float
    number = float(value)

    # Round the number to the nearest integer
    rounded_number = round(number)

    # Check if the number is equidistant from two integers
    if number == rounded_number - 0.5:
        # If it is, round it away from zero
        if number > 0:
            return rounded_number + 1
        else:
            return rounded_number - 1

    # Return the rounded number
    return rounded_number

# Test the function with the provided examples
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15