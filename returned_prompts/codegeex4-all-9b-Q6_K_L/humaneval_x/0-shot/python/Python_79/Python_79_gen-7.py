def decimal_to_binary(decimal):
    return "db" + bin(decimal)[2:] + "db"

# Test cases
print(decimal_to_binary(15))   # returns "db1111db"
print(decimal_to_binary(32))   # returns "db100000db"