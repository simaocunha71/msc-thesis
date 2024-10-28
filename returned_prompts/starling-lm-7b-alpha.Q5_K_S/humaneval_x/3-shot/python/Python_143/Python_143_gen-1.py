    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    words = sentence.split(" ")
    result = ""

    for word in words:
        if len(word) == 1 or len(word) == 2 or len(word) == 3 or len(word) == 5 or len(word) == 7 or len(word) == 11:
            result += word + " "

    return result.strip()


