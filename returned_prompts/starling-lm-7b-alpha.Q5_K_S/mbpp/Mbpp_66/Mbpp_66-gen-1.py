```
def pos_count(l):
    count = 0
    for i in l:
        if i > 0:
            count += 1
    return count
```

Explanation:
To solve the problem, we can create a function called pos_count that takes a list as an input. Inside the function, we initialize a variable called count to 0, which will keep track of the number of positive numbers in the list. We then iterate through each element in the list using a for loop. For each element, we check if it is greater than 0 (i.e., a positive number). If it is, we increment the count variable by 1. Finally, we return the count variable, which will give us the total number of positive numbers in the list.

To test the function, we use the assert statement to check if the function correctly counts the number of positive numbers in the given list [1, -2, 3, -4]. In this case, the expected output is 2, as there are two positive numbers (1 and 3) in the list. If the function correctly counts the positive numbers, the assert statement will pass and no error will be raised.

Overall, the solution provides a simple and efficient way to count the number of positive numbers in a given list using Python.


























































































```
def pos_count(l):
    count = 0
    for i in l:
        if i > 0:
            count += 1
    return count
```