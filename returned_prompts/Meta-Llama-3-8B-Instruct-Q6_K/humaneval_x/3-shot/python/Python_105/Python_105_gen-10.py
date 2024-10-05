    def num2word(n):
        if n == 1:
            return "One"
        elif n == 2:
            return "Two"
        elif n == 3:
            return "Three"
        elif n == 4:
            return "Four"
        elif n == 5:
            return "Five"
        elif n == 6:
            return "Six"
        elif n == 7:
            return "Seven"
        elif n == 8:
            return "Eight"
        elif n == 9:
            return "Nine"

    result = []
    for num in sorted([n for n in arr if 1 <= n <= 9]):
        result.append(num2word(num))
    return result[::-1] if result else []  # return empty list if input array is empty


