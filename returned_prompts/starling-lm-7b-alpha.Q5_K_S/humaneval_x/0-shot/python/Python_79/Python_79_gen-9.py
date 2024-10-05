
def decimal_to_binary(decimal):
    binary = bin(decimal)
    binary = binary[2:]
    binary = "db" + binary + "db"
    return binary

# Test
print(decimal_to_binary(15))
print(decimal_to_binary(32))






def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return "db" + binary + "db"

# Test
print(decimal_to_binary(15))
print(decimal_to_binary(32))



def decimal_to_binary(decimal):
    binary = format(decimal, 'b')
    return "db" + binary + "db"

# Test
print(decimal_to_binary(15))
print(decimal_to_binary(32))



def decimal_to_binary(decimal):
    binary = bin(decimal)[2:].rjust(16,'0')
    return "db" + binary + "db"

# Test
print(decimal_to_binary(15))
print(decimal_to_binary(32))



def decimal_to_binary(decimal):
    binary = bin(decimal)[2:].rjust(16,'0')
    return "db" + binary + "db"

# Test
print(decimal_to_binary(15))
print(decimal_to_binary(32))



def decimal_to_binary(decimal):
    binary = bin(decimal)[2:].rjust(16,'0')
    return "db" + binary + "db"

# Test
print(decimal_to_binary(15))
print(decimal_to_binary(32))



def decimal_to_binary(decimal):
    binary = bin(decimal)[2:].rjust(16,'0')
    return "db" + binary + "db"

# Test
print(decimal_to_binary(15))
print(decimal_