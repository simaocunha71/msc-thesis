def median_numbers(a,b,c):
    # Sort the numbers
    numbers = sorted([a,b,c])
    # If the first and the last numbers are equal, return the second number
    if numbers[0]==numbers[-1]:
        return numbers[1]
    # If the first and the last numbers are not equal, return the median of the first and the last number and the middle number
    else:
        return (numbers[0] + numbers[-1])/2