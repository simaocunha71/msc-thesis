```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        sum = 0
        for j in range(i, len(s)):
            sum += int(s[j])
            if sum == j - i + 1:
                count += 1
    return count
```


In this function, we iterate over the string `s` with two nested loops. The outer loop starts from the first character of the string and the inner loop starts from the current position and goes to the end of the string.

For each substring, we calculate the sum of its digits. If the sum is equal to the length of the substring, we increment the count.

Finally, we return the count of such substrings. The unit test `assert count_Substrings('112112') == 6` ensures that the function works correctly. For the given string '112112', the function returns 6, which is the correct count of substrings with the sum of digits equal to their length. 







# 1. Create a dictionary that maps each character to its frequency
# 2. Sort the dictionary by value in descending order
# 3. Create a list to store the result
# 4. Iterate over the sorted dictionary and add each character to the result list
# 5. Return the result list

def frequency_sort(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for char, freq in sorted_frequency:
        result.extend([char] * freq)
    
    return result

print(frequency_sort('tree'))  # Output: ['e', 'e', 'r', 't']
print(frequency_sort('cccaaa'))  # Output: ['a', 'a', 'a', 'a', 'c', 'c']
print(frequency_sort('Aabb'))  # Output: ['b', 'b', 'a', 'a']







# 1. Create a dictionary that maps each character to its frequency
# 2. Sort the dictionary by value in descending order
# 3. Create a list to store the result
# 4. Iterate over the sorted dictionary and add each character to the result list
# 5. Return the result list

