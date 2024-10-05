    # Convert the given number to binary
    binary_num = bin(N)[2:]

    # Initialize result
    result = ""

    # Iterate through each character in the binary representation
    for char in binary_num:
        # Convert the character to int
        num = int(char)
        # Add 1 to the number
        num += 1
        # Convert the result back to binary
        result += str(bin(num)[2:])

    return result

# Call the function with the given test cases
print(solve(1000)) # "1"
print(solve(150)) # "110"
print(solve(147)) # "1100"

# Call the function with the test cases of your choice
print(solve(100)) # "11000"
print(solve(3)) # "11"
print(solve(0)) # "0"

# Add more test cases of your choice
print(solve(255)) # "11111111"
print(solve(8765)) # "1000111011"
print(solve(12345)) # "1101001001"



# Add more test cases of your choice
print(solve(123456789)) # "11010011000011000001101101"
print(solve(987654321)) # "11001111000011000001100011"
print(solve(4321)) # "10010001"
















































































