
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    
    def helper(s):
        if s:
            x = len(s) - 2
            while x>=0 and not s[x].isdigit():
                x -= 1
            return sum(int(c) for c in s[x:])
        
    return helper("".join([char for char in list(set(s))] + [s]))
