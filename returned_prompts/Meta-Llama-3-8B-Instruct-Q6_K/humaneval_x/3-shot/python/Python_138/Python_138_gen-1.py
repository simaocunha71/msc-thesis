    def is_even(num):
        return num % 2 == 0

    def sum_even_numbers():
        total = 0
        count = 0
        num = n
        while num > 0:
            if is_even(num):
                total += num
                count += 1
            num //= 2
        return total, count

    total, count = sum_even_numbers()
    return count == 4


