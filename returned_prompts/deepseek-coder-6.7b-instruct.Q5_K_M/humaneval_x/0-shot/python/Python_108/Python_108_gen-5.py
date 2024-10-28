
    def sum_digits(n):
        sum = 0
        while n:
            sum += n % 10
            n //= 10
        return sum

    return sum(abs(sum_digits(i)) > 0 for i in arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Expected output:
# TestResult(failed=0, attempted=3)

#task_15.py
