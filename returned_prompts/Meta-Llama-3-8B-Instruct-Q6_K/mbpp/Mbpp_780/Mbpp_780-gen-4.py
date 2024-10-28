```
def find_combinations(tuples_list):
    result = []
    for i in range(len(tuples_list)):
        for j in range(i, len(tuples_list)):
            result.append((tuples_list[i][0] + tuples_list[j][0], tuples_list[i][1] + tuples_list[j][1]))
    return result
```


Explanation:
The problem is asking to write a function that takes a list of tuples as input, where each tuple contains two integers. The function should return a list of new tuples, where each new tuple is a combination of sums of corresponding elements from the input tuples.

The unit test `assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]` helps to clarify the problem. It shows that the function should return all possible combinations of sums of corresponding elements from the input tuples.

The solution uses two nested loops to iterate over the input list of tuples. For each pair of tuples, it creates a new tuple with the sums of corresponding elements and adds it to the result list.

The time complexity of the solution is O(n^2), where n is the length of the input list of tuples. The space complexity is O(n^2) as well, as the result list can contain up to n^2 tuples.