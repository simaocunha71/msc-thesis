```
def find_substring(lst, substring):
    for s in lst:
        if substring in s:
            return True
    return False
```


The function `find_substring` iterates over each string in the list `lst`. For each string, it checks if the `substring` is present using the `in` operator. If the `substring` is found in any string, the function immediately returns `True`. If the `substring` is not found in any string after checking all strings, the function returns `False`. The unit test `assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True` suggests that the function should return `True` if the substring is present in any string in the list. The function passes this test.