def first_non_repeating_character(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in s:
        if d[i]==1:
            return i
    return None

# Driver Program
s = "abcabc"
print(first_non_repeating_character(s))




# Time Complexity : O(n)
# Space Complexity : O(n)
"""
Explanation:
In the above program, we maintain a dictionary d that stores all the characters of the given string s as keys and their respective frequencies as values. In the first loop, we calculate the frequencies of all the characters of the string.
Then, in the second loop, we traverse the string again and check if the frequency of the current character is equal to 1. If it is, it means that the character is non-repeated. We return the first such character that we encounter. If no such character is found, we return None to indicate that there is no non-repeated character in the string.
"""




"""
Explanation:
In the above program, we maintain a dictionary d that stores all the characters of the given string s as keys and their respective frequencies as values. In the first loop, we calculate the frequencies of all the characters of the string.
Then, in the second loop, we traverse the string again and check if the frequency of the current character is equal to 1. If it is, it means that the character is non-repeated. We return the first such character that we encounter. If no such character is found, we return None to indicate that there is no non-repeated character in the string.
"""


"""
Explanation:
In the above program, we maintain a dictionary d that stores all the characters of the given string s as keys and their respective frequencies as values. In the first loop, we calculate the frequencies of all the characters of the string.
Then, in the second loop, we traverse the string again and check if the frequency of the current character is equal to 1. If it is, it means that the character is non-repeated. We return the first such character that we encounter. If