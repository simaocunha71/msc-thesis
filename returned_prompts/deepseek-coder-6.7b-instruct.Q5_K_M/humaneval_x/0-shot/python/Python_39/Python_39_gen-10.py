
    def prime_fib(n: int):
        if n < 1:
            raise ValueError("Input should be a positive integer.")

        def is_prime(num: int):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def fib(n: int):
            fib_values = [0, 1]
            while len(fib_values) <= n:
                fib_values.append(fib_values[-1] + fib_values[-2])
            return fib_values[n]

        count = 0
        i = 1
        while count < n:
            i += 1
            if is_prime(fib(i)):
                count += 1

        return fib(i)

    return prime_fib(n)


print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(7))
print(prime_fib(8))
print(prime_fib(9))
print(prime_fib(10))


def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 233
    assert prime_fib(7) == 1597
    assert prime_fib(8) == 28657
    assert prime_fib(9) == 514229
    assert prime_fib(10) == 433494437

    with pytest.raises(ValueError):
        prime_fib(0)
    with pytest.raises(ValueError):