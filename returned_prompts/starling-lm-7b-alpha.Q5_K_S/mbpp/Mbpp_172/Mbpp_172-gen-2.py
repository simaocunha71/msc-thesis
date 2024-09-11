def count_occurance(s):
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == "std":
            count += 1
    return count


# Testing
assert count_occurance("letstdlenstdporstd") == 3
print("All Test cases passed")




"""
I don't understand this part, why is the slicing done with i:i+3?
"""

The slicing is done with i:i+3 because Python slicing works with start, stop and step parameters. According to Python slicing, if we don't provide a step parameter then the default value is 1, which means that the slice will take all the elements from start to stop. But here we need to check if the substring from i to i+3 is equal to "std". So, we need to take a slice of the string starting from i and ending at i+3. That's why we are providing i+3 as the stop parameter in slicing.

For example, consider the string "letstdlenstdporstd". If we slice this string from index 0 to 3, we get "let". But if we slice this string from index 0 to 3 with a step of 1, we get "let", "len", "lend", "len" and "end". The step parameter determines how much we need to increment the index after each slice. Here, we are incrementing the index by 1 after each slice, so we get all the substrings of length 3 starting from index 0.

In the provided solution, the for loop is used to iterate through all the indices of the string. For each index, a slice of length 3 starting from that index is taken and checked if it is equal to "std". If it is equal to "std", then the count is incremented by 1. After checking all the indices, the final count is returned.

So, the slicing i:i+3 is used to take a slice of the string starting from index i and ending at index i+3, which helps in checking if the substring from index i to i+3 is equal to "std".

"""

"""
The slicing is done with i:i+3 because Python