def count_Substrings(s):
    count = 0
    n = len(s)
    for length in range(1, n+1):
        for i in range(n-length+1):
            substring = s[i:i+length]
            if sum(int(digit) for digit in substring) == length:
                count += 1
    return count

print(count_Substrings('112112'))  # 6

Explanation:
The function works by iterating over all possible lengths of substrings from 1 to the length of the string. For each length, it iterates over all substrings of that length, checking if the sum of the digits of the substring is equal to the length of the substring. If it is, it increments the count.
The time complexity is O(n^2), where n is the length of the string, because it iterates over all possible substrings. The space complexity is O(n), because it stores the substring.
"""

# Python program to find the sum of digits in a string 
def find_sum(str): 
    temp = "0"
    sum = 0
    for i in str: 
        if (i.isdigit()): 
            temp += i 
        else: 
            sum += int(temp) 
            temp = "0"
    return sum + int(temp) 

print(find_sum("112112"))  # 10

Explanation:
This Python program finds the sum of digits in a string using the isdigit() function. It traverses the string character by character. When it encounters a digit, it concatenates it with a temporary string. When it encounters a non-digit character, it adds the value of the temporary string to the sum and resets the temporary string to "0". The process continues until the end of the string. Finally, it adds the value of the temporary string to the sum because the string might end with a digit.
"""

# Python program to find the sum of digits in a string 
def find_sum(str): 
    sum = 0
    for i in str: 
        if (i.isdigit