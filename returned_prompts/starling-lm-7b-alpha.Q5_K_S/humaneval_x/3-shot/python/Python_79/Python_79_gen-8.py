    def binary(decimal):
        if decimal == 0:
            return "0b0"
        else:
            return "0b" + str(bin(decimal))[2:]

    print(binary(decimal))


