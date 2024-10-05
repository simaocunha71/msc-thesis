    def is_odd(n):
        return n % 2 != 0

    def check_first_and_last(n):
        first = str(n)[0]
        last = str(n)[-1]
        return is_odd(int(first)) and is_odd(int(last))

    count = 0
    for num in nums:
        if num > 10 and check_first_and_last(num):
            count += 1
    return count


