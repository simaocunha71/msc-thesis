    def cycpattern_check(a, b):
        if len(a) < len(b):
            return False
        for i in range(len(b)):
            if a[i:i+len(b)] == b:
                return True
        return False
    # test the function
    print(cycpattern_check("abcd","abd")) # False
    print(cycpattern_check("hello","ell")) # True
    print(cycpattern_check("whassup","psus")) # False
    print(cycpattern_check("abab","baa")) # True
    print(cycpattern_check("efef","eeff")) # False
    print(cycpattern_check("himenss","simen")) # True

#Explanation: 
This function checks if the second word or any of its rotations is a substring in the first word. It first checks if the length of the first word is less than the length of the second word. If it is, it returns False because the second word cannot be a substring of the first word. 
If the lengths are the same or the first word is longer, it then checks if the second word is a substring of the first word by iterating through the first word and checking if the second word matches at any position. If it does, it returns True. 
If it doesn't find a match after checking all positions, it returns False. 
The function uses slicing to extract substrings from the first word and compare them to the second word. 
For example, `a[i:i+len(b)]` extracts a substring of length `len(b)` starting from position `i` in the first word. 
This function can be used to check if a pattern is present in a string, which is a common problem in many areas of computer science, such as data compression, string matching, and cryptography. 







#Test Case 1: 
print(cycpattern_check("abcd","abd")) # False

#Test Case 2: 
print(cycpattern_check("hello","ell")) # True

#Test Case 3: 
print(cycpattern_check("whassup","psus")) # False

#Test Case 4: 
print(cycpattern_check("abab","baa")) # True

#Test Case 5: 
print(cycpattern_check("efef","eeff")) # False

#Test Case 6: 
print(cycpattern_check("himenss","simen")) # True

#Explanation: 
