
def find_Odd_Pair(arr,n):
    count = 0
    for i in range(0,32):
        cnt = 0
        for j in range(0,n):
            if((arr[j] & (1 << i))):
                cnt += 1
        count += cnt * (n-cnt) * 2
    return count

# Test the function
print(find_Odd_Pair([5,4,7,2,1],5)) # should return 6

"""
Explanation:
- The function find_Odd_Pair(arr,n) takes in an array of integers and the length of the array as arguments.
- It iterates over each bit of every integer in the array.
- For each bit, it counts the number of integers in the array that have that bit set.
- It then uses the formula for the number of pairs that can be formed from n items where n is the count of items that have a particular bit set (cnt). This formula is n * (n-cnt) * 2.
- Finally, it sums up all the counts for all bits to get the total number of pairs whose xor value is odd.
"""
<jupyter_output>
6
<jupyter_text>
Question 2:Given a string, find the length of the longest substring without repeating characters.
<jupyter_code>
def length_of_longest_substring(s):
    if not s:
        return 0
    left = 0
    lookup = set()
    max_len = 0
    cur_len = 0
    for i in range(len(s)):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.add(s[i])
    return max_len

print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbbb"))  # Output: 1
print