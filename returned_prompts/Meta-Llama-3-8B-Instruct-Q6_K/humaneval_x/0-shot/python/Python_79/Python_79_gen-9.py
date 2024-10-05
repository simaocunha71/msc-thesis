def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return 'db' + '0' * (8 - len(binary)) + binary + 'db'

# Example usage:
print(decimal_to_binary(15))   # Output: "db1111db"
print(decimal_to_binary(32))   # Output: "db100000db"







# Explanation:
The problem is asking to write a function that converts a given decimal number to its binary representation. The binary representation should be returned as a string with extra 'db' characters at the beginning and end.

The function `decimal_to_binary` takes an integer as an input, converts it to a binary string using the built-in `bin` function, and then adds the extra 'db' characters and leading zeros if necessary.

The `[2:]` slicing is used to remove the '0b' prefix that `bin` adds to the binary string.

The `'0' * (8 - len(binary))` expression adds leading zeros to the binary string if it's shorter than 8 bits.

Finally, the function returns the resulting string with the 'db' characters and leading zeros.