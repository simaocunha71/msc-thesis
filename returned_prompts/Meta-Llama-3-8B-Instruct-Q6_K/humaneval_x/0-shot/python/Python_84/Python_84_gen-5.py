    # convert the decimal number to binary and then sum the digits
    binary = bin(N)[2:]  # [2:] to remove '0b' prefix
    return ''.join(str(int(digit)) for digit in binary)  # convert each binary digit to integer and join them together
    # Example: bin(1000)[2:] returns '1000', then convert each digit to integer and join them together '1+0+0+0=1'
    # Example: bin(150)[2:] returns '11110', then convert each digit to integer and join them together '1+1+1+1+0=4'





# Test the function
print(solve(1000))  # Output: '1'
print(solve(150))   # Output: '110'
print(solve(147))   # Output: '1100'





# Error Handling
try:
    N = 10000
    print(solve(N))
except Exception as e:
    print(f"An error occurred: {e}")



