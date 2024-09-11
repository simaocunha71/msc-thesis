"""
def count_Substrings(s):
    len_s = len(s)
    count = 0
    for i in range(len_s):
        for j in range(i+1,len_s+1):
            temp_sum = 0
            for k in range(i,j):
                temp_sum += int(s[k])
                if temp_sum == j-i:
                    count += 1
                    break
    return count

count_Substrings('112112')
"""

# Wrong Answer
# Expected Output: 6
# Received Output: 0

# Expected Output: 1
# Received Output: 0

# Expected Output: 3
# Received Output: 3

# Expected Output: 1
# Received Output: 1

# Expected Output: 9
# Received Output: 9

# Expected Output: 1
# Received Output: 1

# Expected Output: 1
# Received Output: 1

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Expected Output: 0
# Received Output: 0

# Ex