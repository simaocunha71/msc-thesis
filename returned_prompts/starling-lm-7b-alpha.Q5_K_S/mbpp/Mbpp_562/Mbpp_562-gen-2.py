"""
def Find_Max_Length(input_list):
    max_length = 0
    for sublist in input_list:
        if len(sublist) > max_length:
            max_length = len(sublist)
    return max_length

print(Find_Max_Length([[1],[1,4],[5,6,7,8]]))
"""

def Find_Max_Length(input_list):
    max_length = 0
    for sublist in input_list:
        if len(sublist) > max_length:
            max_length = len(sublist)
    return max_length

print(Find_Max_Length([[1],[1,4],[5,6,7,8]]))


"""
In this code, we define a function called Find_Max_Length which takes an input list as its parameter. We initialize the max_length variable to 0. Then we iterate through each sublist in the input list. For each sublist, we compare the length of the sublist to the current max_length. If the length of the sublist is greater than the max_length, we update the max_length to the length of the sublist. Finally, we return the max_length after all sublists have been processed.

When we run this code with the test case provided, we get the correct output of 4, which is the length of the longest sublist in the input_list.
"""


"""
Here's a breakdown of the code:

1. We define a function called Find_Max_Length that takes an input_list as its parameter.
2. We initialize the max_length variable to 0. This variable will store the length of the longest sublist.
3. We use a for loop to iterate through each sublist in the input_list.
4. Inside the loop, we compare the length of the current sublist to the current max_length. If the length of the sublist is greater than the max_length, we update the max_length to the length of the sublist.
5. After all sublists have been processed, we return the max_length.

The function is then called with the input_list [[1],[1,4],[