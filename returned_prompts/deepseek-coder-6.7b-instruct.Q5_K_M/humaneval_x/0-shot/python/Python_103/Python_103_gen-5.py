
def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        avg = (n + m) // 2
        return bin(avg)

print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"
print(rounded_avg(0, 0))  # => "0b0"
print(rounded_avg(1, 1))  # => "0b1"
print(rounded_avg(2, 3))  # => "0b11"
print(rounded_avg(3, 5))  # => "0b11"
print(rounded_avg(5, 7))  # => "0b111"
print(rounded_avg(7, 9))  # => "0b111"
print(rounded_avg(9, 11))  # => "0b1011"
print(rounded_avg(11, 13))  # => "0b1101"
print(rounded_avg(13, 15))  # => "0b1111"
print(rounded_avg(15, 17))  # => "0b11111"
print(rounded_avg(17, 19))  # => "0b11111"
print(rounded_avg(19, 21))  # => "0b10101"
print(rounded_avg(21, 23))  # => "0b10111"
print(rounded_avg(23, 25))  # => "0b11001"
print(rounded_avg