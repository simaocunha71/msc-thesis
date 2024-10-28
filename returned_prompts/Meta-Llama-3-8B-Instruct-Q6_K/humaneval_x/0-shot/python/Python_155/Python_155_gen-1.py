    def even_odd_count(num):
        even_count = 0
        odd_count = 0
        for digit in str(abs(num)):
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return (even_count, odd_count)  # return the counts as a tuple


# Test cases
print(even_odd_count(-12))  # (1, 1)
print(even_odd_count(123))  # (1, 2)
print(even_odd_count(246))  # (2, 0)
print(even_odd_count(135))  # (0, 3)

# You can test the function with more numbers if you want.