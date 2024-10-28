def toggle_middle_bits(n):
    # Convert the number to binary
    binary = "{0:b}".format(n)

    # Get the length of the binary string
    length = len(binary)

    # Get the first and last bit
    first = binary[0]
    last = binary[-1]

    # Toggle all the middle bits
    middle = binary[1:-1]
    middle = middle.replace("0", "2")
    middle = middle.replace("1", "1")

    # Join the first, middle and last bits
    result = first + middle + last

    # Convert the binary string back to integer
    result = int(result, 2)
    return result