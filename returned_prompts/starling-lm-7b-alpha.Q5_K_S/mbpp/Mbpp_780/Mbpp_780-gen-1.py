"""
def find_combinations(tup_list):
    result = []
    for i in range(len(tup_list)):
        for j in range(len(tup_list)):
            result.append((tup_list[i][0] + tup_list[j][0], tup_list[i][1] + tup_list[j][1]))
    return result

find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)])

"""

def find_combinations(tup_list):
    result = []
    for i in range(len(tup_list)):
        for j in range(i + 1, len(tup_list)):
            result.append((tup_list[i][0] + tup_list[j][0], tup_list[i][1] + tup_list[j][1]))
    return result

find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)])

# Time complexity: O(n^2)
# Space complexity: O(1)

# The above code has a time complexity of O(n^2) and a space complexity of O(1). This is because the time complexity is determined by the nested for loops, which iterate over the entire length of the tuple list twice. The space complexity is determined by the number of elements in the result list, which does not depend on the size of the input.

# Here's a step-by-step breakdown of the code:

# The function find_combinations takes a tuple list as input and returns a list of tuples.
# The result variable is initialized as an empty list to store the combinations.
# The outer for loop iterates over the indices of the tuple list.
# The inner for loop iterates over the indices of the tuple list, starting from the next index after the current index. This ensures that each combination is only calculated once and not repeated.
# Inside the inner loop, the sum of the first elements and the second elements of the current and next tuples are calculated and added as a tuple to the result