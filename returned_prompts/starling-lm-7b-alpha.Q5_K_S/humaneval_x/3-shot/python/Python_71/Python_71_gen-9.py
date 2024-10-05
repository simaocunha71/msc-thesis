    def heron(a, b, c):
        """ Heron's formula to calculate the area of the triangle given the lengths of its sides """
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

    if (a + b > c) and (a + c > b) and (b + c > a):
        return round(heron(a, b, c), 2)
    else:
        return -1


