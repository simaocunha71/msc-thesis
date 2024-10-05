    def mini_roman(number):
        numerals = ["i", "v", "x", "l", "c", "d", "m"]
        values = [1, 5, 10, 50, 100, 500, 1000]
        result = ""
        for i in range(len(values)):
            while number >= values[i]:
                result += numerals[i]
                number -= values[i]
        return result

    return mini_roman(number)


