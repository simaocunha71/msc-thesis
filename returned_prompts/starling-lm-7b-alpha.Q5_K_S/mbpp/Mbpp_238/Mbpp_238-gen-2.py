def number_of_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            count += 1
    return count


# assert number_of_substrings("abc") == 6

def number_of_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            count += 1
    return count


number_of_substrings("abc") # 6



"""
The function works by iterating over each letter in the string. For each letter, it counts all the possible substrings that can be formed starting from that letter. The first loop (for i in range(n)) selects the starting index of the substring. The second loop (for j in range(i+1, n+1)) selects the end index of the substring, creating all possible substrings starting at index i. The variable count is incremented for each substring formed, and returned at the end of the function.
"""

































"""
In the Python programming language, a substring is a contiguous sequence of one or more characters within a string. Here are some examples of substrings in the string "hello":

The entire string is itself a substring: "hello"
Each individual character is a substring: "h", "e", "l", "l", "o"
A single character followed by the next character: "he", "el", "lo"
A sequence of multiple characters: "hel", "ell", "llo"

The number of possible substrings in a string is determined by the length of the string itself. This is because each character in the string can be combined with every other character to form a substring. For example, in a string of length 3, there are 3 * 3 * 3 = 27 possible substrings. However, some of these substrings may be identical, such as "a" in the string "aaa". To