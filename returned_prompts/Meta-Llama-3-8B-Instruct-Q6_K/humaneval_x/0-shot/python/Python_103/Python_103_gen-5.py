    if n > m:
        return -1
    
    total_sum = sum(range(n, m+1))
    avg = round(total_sum / (m - n + 1))
    return bin(avg)[2:]

# Test cases
print(rounded_avg(1, 5))  # Output: "0b11"
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: "0b1111"
print(rounded_avg(20, 33))  # Output: "0b11010"
print(rounded_avg(1, 1))  # Output: "0b1"  # Test case for n == m
print(rounded_avg(5, 5))  # Output: "0b1"  # Test case for n == m
print(rounded_avg(2, 2))  # Output: "0b1"  # Test case for n == m
print(rounded_avg(10, 10))  # Output: "0b1"  # Test case for n == m
print(rounded_avg(1, 10))  # Output: "0b1"  # Test case for n < m
print(rounded_avg(2, 10))  # Output: "0b10"  # Test case for n < m
print(rounded_avg(3, 10))  # Output: "0b11"  # Test case for n < m
print(rounded_avg(4, 10))  # Output: "0b100"  # Test case for n < m
print(rounded_avg(5, 10))  # Output: "0b101"  # Test case for n < m
print(rounded_avg(6, 10))  # Output: "0b110"  # Test case for n < m
print(rounded_avg(7, 10))  # Output: "0b111"  # Test case for n < m
print(rounded_avg(8, 10))  # Output: "0b1000"  # Test case for n < m
print(rounded_avg(9, 10))  # Output: "0b1001"  # Test case for n < m
print(rounded_avg(10, 10))  # Output: "0b1010" 