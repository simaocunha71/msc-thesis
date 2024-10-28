    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    words = sentence.split(" ")
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)


