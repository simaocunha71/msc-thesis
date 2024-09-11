def count_reverse_pairs(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(i+1,len(string_list)):
            if string_list[i] == string_list[j][::-1]:
                count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
# print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))



"""
Given an array of strings, count the number of pairs of strings in the array
which are reverse of each other.

For example, if the given array is ['julia', 'best', 'tseb', 'for', 'ailuj']
then the output should be 2. Because 'tseb' is the reverse of 'best'
and 'ailuj' is the reverse of 'julia'.

"""


def count_reverse_pairs(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(i+1,len(string_list)):
            if string_list[i] == string_list[j][::-1]:
                count += 1
    return count

# assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
# print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))



```

The code defines a function `count_reverse_pairs` that takes in a list of strings and returns the count of pairs of reverse strings in the list. It uses two nested loops to compare each pair of strings and checks if the second string is the reverse of the first string. If it is, the count is incremented by 1. Finally, the function returns the count. The code includes an assertion to test the function with a sample input and prints the result of the function with the same sample input.
```
