    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    words = sentence.split(" ")
    result = ""
    for word in words:
        if len(word) > 1 and is_prime(len(word)):
            result += word + " "
    return result.strip()


