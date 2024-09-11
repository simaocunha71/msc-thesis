from itertools import combinations

def find_combinations(tuples):
    combinations_list = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            combinations_list.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return combinations_list

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))



"""
The function find_combinations takes a tuple list as the argument and returns a list of tuples of sums. The function uses two for loops to iterate through the tuple list. For each tuple in the list, it appends a new tuple to the combinations_list, where the first element is the sum of the first elements of the two tuples, and the second element is the sum of the second elements of the two tuples. The resulting combinations_list is then returned by the function.
"""







"""
def find_combinations(tuples):
    combinations_list = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            combinations_list.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return combinations_list

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
"""



"""
In this solution, the function find_combinations takes a tuple list as the argument and returns a list of tuples of sums. The function uses a nested for loop to iterate through the tuple list. For each tuple in the list, it appends a new tuple to the combinations_list, where the first element is the sum of the first elements of the two tuples, and the second element is the sum of the second elements of the two tuples. The resulting combinations_list is then returned by the function.
"""


"""
In this solution, the function find_com