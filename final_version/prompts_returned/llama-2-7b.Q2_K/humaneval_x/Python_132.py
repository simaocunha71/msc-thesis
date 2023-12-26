
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    
    if len(string) == 0:
        return False # base condition, nothing to do
        
    if '[' in string and '[[' not in string:
        first = string.find('[') + 1
        if first != -1:
            return is_nested(string[:first])
        
        elif len(string) == 2: # if we're at the last bracket and there aren't any nested brackets, it must be valid
            # e.g., '[[]]', '[[]]]', '[[]]', or '[]'.
            return True
        
    elif '[' not in string and '[[' in string:
        last = string.find(']') + 1
        if last != -1:
            return is_nested(string[:last])   # and we're at the first bracket, check nestedness of its contents again
        
    elif len(string) == 2: # else there are no nestings
        if '[' in string and '[[' in string:
            ndx = string.find(']') + 1
            return True                              # at least one bracket in our subsequence is nested, but we don't know which
        elif len(string) == 3: # two brackets but no nestings? maybe the last bracket is its own contents (no matter what comes after [[]])
            ndx = string.find(']') + 1 + string.rfind('[') + 1   # find index of nested