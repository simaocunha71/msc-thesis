def count_reverse_pairs(s_list):
    pairs = 0
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):
            if s_list[i] == s_list[j][::-1]:
                pairs += 1
    return pairs

# Test
print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))  # 2




"""
In the given function, we initialize a variable "pairs" to keep track of the number of reverse pairs. We then use two nested loops to compare each string in the list with all the other strings. For each pair of strings, we check if the first string is equal to the reverse of the second string. If it is, we increment the "pairs" variable. Finally, we return the value of the "pairs" variable.

The time complexity of this function is O(n^2), where n is the length of the input list. This is because we are using two nested loops to compare each pair of strings. The space complexity of this function is O(1), as we only use a single variable to keep track of the number of reverse pairs.
"""

# Python3 program to count pairs of
# reverse strings in a list of strings

# Function to count pairs of reverse
# strings in a list of strings
def count_reverse_pairs(s_list):
    # Initialize pairs to 0
    pairs = 0

    # Compare each string in the list
    # with all other strings
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):

            # If strings are reverse of each other
            if s_list[i] == s_list[j][::-1]:
                # Increment pairs
                pairs += 1

    # Return pairs
    return pairs

# Driver program
if __name__ == "__main__":
    # Input list of strings
    s_list = ["julia", "best", "tseb", "for", "ailuj"]

    # Function call
    print