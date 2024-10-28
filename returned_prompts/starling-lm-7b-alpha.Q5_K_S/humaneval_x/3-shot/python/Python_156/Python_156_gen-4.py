    def int_to_mini(number):
        if number < 0:
            raise ValueError("The input number must be non-negative")
        if number > 1000:
            raise ValueError("The input number must be between 1 and 1000")
        result = []

        while number > 0:
            if number >= 1000:
                result.append("m")
                number -= 1000
            elif number >= 900:
                result.append("cm")
                number -= 900
            elif number >= 500:
                result.append("d")
                number -= 500
            elif number >= 400:
                result.append("cd")
                number -= 400
            elif number >= 100:
                result.append("c")
                number -= 100
            elif number >= 90:
                result.append("xc")
                number -= 90
            elif number >= 50:
                result.append("l")
                number -= 50
            elif number >= 40:
                result.append("xl")
                number -= 40
            elif number >= 10:
                result.append("x")
                number -= 10
            elif number >= 9:
                result.append("ix")
                number -= 9
            elif number >= 5:
                result.append("v")
                number -= 5
            elif number >= 4:
                result.append("iv")
                number -= 4
            elif number >= 1:
                result.append("i")
                number -= 1

        return "".join(result)

    return int_to_mini(number)


