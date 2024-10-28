
    if n > m:
        return -1
    else:
        avg = (n + m) / 2
        rounded_avg = round(avg)
        binary = bin(rounded_avg)
        return binary

print(rounded_avg(1, 5)) # => "0b11"
print(rounded_avg(7, 5)) # => -1
print(rounded_avg(10, 20)) # => "0b1111"
print(rounded_avg(20, 33)) # => "0b11010"

# -----------------------------------

# 2. Write a function that takes a list of integers and a number, then returns a list of all pairs of integers in the list that sum up to the number.

