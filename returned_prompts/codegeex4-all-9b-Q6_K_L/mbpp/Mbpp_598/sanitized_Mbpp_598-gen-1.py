def armstrong_number(n):
    # Convert the number to a list of digits
    digits = [int(d) for d in str(n)]
    # Check if the sum of the cubes of the digits is equal to the number
    return n == sum([d**3 for d in digits])