def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round(sum(range(n, m + 1)) / (m - n + 1))
    return bin(avg)

print(rounded_avg(1, 5)) # "0b11"
print(rounded_avg(7, 5)) # -1
print(rounded_avg(10, 20)) # "0b1111"
print(rounded_avg(20, 33)) # "0b11010"

The function rounded_avg takes two arguments, n and m. If n is greater than m, the function returns -1. Otherwise, it computes the average of the integers from n through m (including n and m) by summing the range of numbers from n to m and dividing by the number of integers in the range. The average is then rounded to the nearest integer using the round function. Finally, the average is converted to binary using the bin function and returned as a string.