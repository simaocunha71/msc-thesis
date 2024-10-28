def decimal_to_binary(decimal):
    return "db" + bin(decimal)[2:] + "db"

print(decimal_to_binary(15))
print(decimal_to_binary(32))