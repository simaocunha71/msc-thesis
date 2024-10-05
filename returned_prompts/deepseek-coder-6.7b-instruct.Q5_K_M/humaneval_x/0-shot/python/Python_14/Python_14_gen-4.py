def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[0:i+1])
    return prefixes


print(all_prefixes('abc'))


"""
In this solution, we create an empty list prefixes to store all the prefixes of the string. Then we iterate over the string using a loop that goes from 0 to len(string) - 1. For each iteration, we append the substring from the start of the string to the i-th character to the list prefixes. Finally, we return the list prefixes.
"""

# Question 4:

