    def decimal_to_binary(decimal):
        binary_string = ""
        while decimal != 0:
            remainder = decimal % 2
            decimal = decimal // 2
            binary_string += str(remainder)
        binary_string = "db" + "0" * (len(binary_string) // 4) + binary_string + "db"
        return binary_string


