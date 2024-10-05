
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return "db" + binary + "db"

def decimal_to_binary_v2(decimal):
    return "db" + bin(decimal)[2:].zfill(32) + "db"
