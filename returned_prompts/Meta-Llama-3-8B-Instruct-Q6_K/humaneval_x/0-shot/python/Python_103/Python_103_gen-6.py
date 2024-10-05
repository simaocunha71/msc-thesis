def rounded_avg(n, m):
    if n > m:
        return -1
    
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    return bin(rounded_avg)[2:]

print(rounded_avg(1, 5)) # "0b11"
print(rounded_avg(7, 5)) # -1
print(rounded_avg(10, 20)) # "0b1111"
print(rounded_avg(20, 33)) # "0b11010" 





Note: The function rounded_avg takes two arguments n and m and returns the binary representation of the rounded average of the numbers from n to m. If n is greater than m, it returns -1. The function uses the built-in Python functions round and bin to compute and format the result. The bin function returns a string that starts with "0b" to indicate that it is a binary number, so we use [2:] to remove the first two characters.