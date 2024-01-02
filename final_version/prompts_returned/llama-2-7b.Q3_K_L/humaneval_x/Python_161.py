
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
    
    def is_letter(char):
        return char >= 'A' and char <= 'Z' or char >= 'a' and char <= 'z'
        
    def reverse_case_of_char(char, upper=True):
        if is_letter(char) and upper:
            return chr((ord(char) - ord('A') + ord('a')) & 255)
        elif is_letter(char) and not upper:
            return chr((ord(char) - ord('Z') + ord('a')) & 255)
        else:
            return char
    
    def find_all_letters(s):
        letters = set()
        for i, c in enumerate(s):
            if is_letter(c):
                letters.add(c)
                
        return sorted(list(letters))
        
    def get_first_letter(s):
        return s[0]
    
    def get_reverse_char(s, char):
        if is_letter(char):
            if upper:=get_case(char) == "upper":
                return reverse_case_of_char(char, False)
            else:
                return reverse_case_of_char(char, True)
        
    def get_case(letters[0]):
        if letters[0][1].lower() < letters[0][2].lower():  # upper to lower case -> lower to upper case
            return "upper"
        else:
            return "lower"
    
    def get_last_letter(s, char):
        if char == 'Z' and s[-1] == 'A':
            return '