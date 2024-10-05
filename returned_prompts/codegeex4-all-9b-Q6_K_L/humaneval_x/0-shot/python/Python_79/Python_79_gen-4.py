def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove the '0b' prefix
    return 'db' + binary + 'db'  # Add the 'db' prefix and suffix

print(decimal_to_binary(15))  # "db1111db"
print(decimal_to_binary(32))  # "db100000db"