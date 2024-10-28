```
def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for char in s:
        if char.isupper():
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 0
    return max(max_run, current_run)
``` 
This function iterates over the input string, counting the length of each run of uppercase characters. It keeps track of the maximum run seen so far and updates it whenever it encounters a run that is longer. At the end of the function, it returns the maximum run found, or the current run if it is longer than the maximum run. 

The unit test `assert max_run_uppercase('GeMKSForGERksISBESt') == 5` ensures that the function works correctly by testing it on a string that contains multiple runs of uppercase characters.  The function should return 5, which is the length of the longest run of uppercase characters in the string. 

The time complexity of this function is O(n), where n is the length of the input string, because it iterates over the string once. The space complexity is O(1), because it uses a constant amount of space to store the maximum run and the current run. 