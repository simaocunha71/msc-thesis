def perfect_squares(start, end):
    return [i**2 for i in range(int(start**0.5), int(end**0.5)+1) if start <= i**2 <= end]  # or use math.sqrt() and int() for more precision
    # or use a list comprehension with if condition to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(math.sqrt(start)), int(math.sqrt(end))+1) if start <= i**2 <= end]  # using math.sqrt() for more precision
    # or use a list comprehension with if condition to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(end**0.5), int(start**0.5)-1, -1) if start <= i**2 <= end]  # using list comprehension with reverse order to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(math.sqrt(end)), int(math.sqrt(start))+1) if start <= i**2 <= end]  # using list comprehension with if condition to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(end**0.5), int(math.sqrt(start))+1) if start <= i**2 <= end]  # using list comprehension with if condition to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(math.sqrt(end)), int(math.sqrt(start))+1) if start <= i**2 <= end]  # using list comprehension with if condition to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(math.sqrt(end)), int(math.sqrt(start))+1) if start <= i**2 <= end]  # using list comprehension with if condition to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(math.sqrt(end)), int(math.sqrt(start))+1) if start <= i**2 <= end]  # using list comprehension with if condition to filter out the numbers that are not perfect squares within the given range
    # return [i**2 for i in range(int(math.sqrt(end)), int(math.sqrt(start))+1) if