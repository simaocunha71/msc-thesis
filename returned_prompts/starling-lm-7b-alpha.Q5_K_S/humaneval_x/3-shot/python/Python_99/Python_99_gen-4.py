    def closest_integer(value):
        number = float(value)
        if number.is_integer():
            return int(number)
        if number > 0:
            return int(number + 0.5)
        else:
            return int(number - 0.5)


