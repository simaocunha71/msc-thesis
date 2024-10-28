def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary = "db" + binary + "db"
    return binary
# Test the function
print(decimal_to_binary(15))   # Output: "db1111db"
print(decimal_to_binary(32))   # Output: "db100000db"  # Test the function
print(decimal_to_binary(10))   # Output: "db1010db"  # Test the function
print(decimal_to_binary(25))   # Output: "db110001db"  # Test the function
print(decimal_to_binary(0))    # Output: "dbdb"  # Test the function
print(decimal_to_binary(1))    # Output: "db1db"  # Test the function
print(decimal_to_binary(2))    # Output: "db10db"  # Test the function
print(decimal_to_binary(3))    # Output: "db11db"  # Test the function
print(decimal_to_binary(4))    # Output: "db100db"  # Test the function
print(decimal_to_binary(5))    # Output: "db101db"  # Test the function
print(decimal_to_binary(6))    # Output: "db110db"  # Test the function
print(decimal_to_binary(7))    # Output: "db111db"  # Test the function
print(decimal_to_binary(8))    # Output: "db1000db"  # Test the function
print(decimal_to_binary(9))    # Output: "db1001db"  # Test the function
print(decimal_to_binary(10))   # Output: "db1010db"  # Test the function
print(decimal_to_binary(11))   # Output: "db1011db"  # Test the function
print(decimal_to_binary(12))   # Output: "db1100db"  # Test the function
print(decimal_to_binary(13))   # Output: "db1101db"  # Test the function
print(decimal_to_binary(14))   # Output: "db1110db"  # Test the function
print(decimal_to_binary(15))   # Output: "db1111db"  # Test the function
print(decimal_to_binary(16))   # Output: "db10000db"  # Test the function
print(decimal_to_binary(17))   #