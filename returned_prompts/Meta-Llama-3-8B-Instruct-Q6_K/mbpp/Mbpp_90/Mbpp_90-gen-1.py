```
def len_log(words):
    return max(len(word) for word in words)
```


Explanation:
The problem is asking for a function that takes a list of words and returns the length of the longest word in that list. 

The unit test provided helps to clarify the problem: `assert len_log(["python","PHP","bigdata"]) == 7`. This test suggests that the function should return the length of the longest word in the list, which in this case is "bigdata" with a length of 7.

The solution uses a generator expression to iterate over each word in the list, calculate its length, and then use the built-in `max` function to find the maximum length. 

For example, if the input list is ["python","PHP","bigdata"], the function will calculate the lengths of each word (8, 3, 7 respectively) and then return the maximum length, which is 8. However, according to the unit test, the expected output is 7, which is the length of the longest word "bigdata". Therefore, the solution is incorrect.

To fix this, we can modify the solution to return the maximum length instead of the maximum length plus one:
```
def len_log(words):
    return max(len(word) for word in words)
```
This solution passes the provided unit test. 