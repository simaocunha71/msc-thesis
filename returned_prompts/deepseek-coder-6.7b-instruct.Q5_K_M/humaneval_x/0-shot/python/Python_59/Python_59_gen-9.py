
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


# ------------------

# Case 1:
print(largest_prime_factor(13195))  # 29

# Case 2:
print(largest_prime_factor(2048))  # 2

# Case 3:
print(largest_prime_factor(60))  # 5

# Case 4:
print(largest_prime_factor(13195))  # 29

# Case 5:
print(largest_prime_factor(2048))  # 2

# Case 6:
print(largest_prime_factor(60))  # 5

# Case 7:
print(largest_prime_factor(13195))  # 29

# Case 8:
print(largest_prime_factor(2048))  # 2

# Case 9:
print(largest_prime_factor(60))  # 5

# Case 10:
print(largest_prime_factor(13195))  # 29

# Case 11:
print(largest_prime_factor(2048))  # 2

# Case 12:
print(largest_prime_factor(60))  # 5

# Case 13:
print(largest_prime_factor(13195))  # 29

# Case 14:
print(largest_prime_factor(2048))  # 2

# Case 15:
print(largest_prime_factor(60))  # 5

# Case 16:
print(largest_prime_factor(13195))  # 29

# Case 17:
print(largest_prime_factor(2048))  # 2

# Case 18:
print(largest