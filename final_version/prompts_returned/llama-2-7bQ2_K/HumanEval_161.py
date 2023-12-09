
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    
    def reverse_case(s):
        """reverse_case -> string -> string"""
        if 'a' <= s[i] <= 'z':  # lower letters to upper case
            return s[:i].upper() + s[i:].lower()
        
        elif 'A' <= s[i] <= 'Z':  # upper letteres to lower case 
            return s[:i].lower() + s[i:].upper()
        
        else: 
            print('error')
            exit(1)
    print("solve -> reverse_case -> string -> string")
    def solve_2():  
        pass
    return solve_2()    
