def prime_length(string):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True       
    return is_prime(len(string))

print(prime_length('Hello')) # True
print(prime_length('abcdcba')) # True
print(prime_length('kittens')) # True
print(prime_length('orange')) # False