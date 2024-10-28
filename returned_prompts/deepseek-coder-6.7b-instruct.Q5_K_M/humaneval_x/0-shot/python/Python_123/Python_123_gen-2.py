
def get_odd_collatz(n):
    def collatz(n):
        result = []
        while n != 1:
            result.append(n)
            n = n // 2 if n % 2 == 0 else n * 3 + 1
        result.append(1)
        return result

    return sorted([i for i in collatz(n) if i % 2 != 0])

print(get_odd_collatz(5))  # [1, 5]



# Test cases
print(get_odd_collatz(1))  # [1]
print(get_odd_collatz(2))  # [1, 2]
print(get_odd_collatz(3))  # [1, 3]
print(get_odd_collatz(4))  # [1, 4]
print(get_odd_collatz(7))  # [1, 7]
print(get_odd_collatz(8))  # [1, 4]
print(get_odd_collatz(9))  # [1, 9]
print(get_odd_collatz(10))  # [1, 5, 10]
print(get_odd_collatz(11))  # [1, 11]
print(get_odd_collatz(15))  # [1, 5, 15]
print(get_odd_collatz(20))  # [1, 5, 11, 20]
print(get_odd_collatz(23))  # [1, 5, 11, 23]
print(get_odd_collatz(30))  # [1, 5, 11, 21, 30]
print(get_odd_collatz(40))  # [1, 5, 11, 21, 30]
print(get_odd_collatz(100))  # [1, 5, 11, 21, 30, 4