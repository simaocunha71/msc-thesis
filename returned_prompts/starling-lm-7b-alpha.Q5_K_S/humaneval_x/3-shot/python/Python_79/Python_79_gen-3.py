    def decimal_to_binary(decimal):
        binary = bin(decimal)[2:]
        binary = "db" + "0" * (4 - len(binary)) + binary + "db"
        return binary


