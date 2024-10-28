```
def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) > 0
```


In this function, we iterate over the input string and use a stack to keep track of the opening brackets. When we encounter a closing bracket, we check if the stack is empty. If it is, we return False because there is no matching opening bracket. If the stack is not empty, we pop the opening bracket from the stack. After iterating over the entire string, we check if the stack is not empty. If it is, it means there are unmatched opening brackets, so we return True. Otherwise, we return False. 

This function works because a nested subsequence of brackets must have at least one opening bracket that is not matched by a closing bracket. If we can find such an opening bracket, it means the subsequence is nested. If we cannot find such an opening bracket, it means the subsequence is not nested. 

The time complexity of this function is O(n), where n is the length of the input string, because we iterate over the string once. The space complexity is O(n) as well, because in the worst case, we might need to store all the opening brackets in the stack. 