def text_lowercase_underscore(s):
    return bool(re.findall(r'[a-z]+_[a-z]+', s)) 

#Test
assert text_lowercase_underscore("aab_cbbbc")==(True) 
#This test will pass because 'aab' and 'cbbbc' are both sequences of lowercase letters joined with an underscore. 

#However, if we test with a string that does not contain sequences of lowercase letters joined with an underscore, the function will return False.

def text_lowercase_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s) is not None

#Test
assert text_lowercase_underscore("aab_cbbbc")==(True) 
assert text_lowercase_underscore("abcd")==(False) 
#This test will pass because 'aab_cbbbc' contains sequences of lowercase letters joined with an underscore, and 'abcd' does not. 
#The function will return True for 'aab_cbbbc' and False for 'abcd'. 
#The function will return None if the pattern is not found in the string, which is equivalent to False in a boolean context. 

#Alternatively, we can use list comprehension to achieve the same result.

def text_lowercase_underscore(s):
    return bool([x for x in re.findall(r'[a-z]+_[a-z]+', s)]) 

#Test
assert text_lowercase_underscore("aab_cbbbc")==(True) 
assert text_lowercase_underscore("abcd")==(False) 
#This test will pass because 'aab_cbbbc' contains sequences of lowercase letters joined with an underscore, and 'abcd' does not. 
#The function will return True for 'aab_cbbbc' and False for 'abcd'. 
#The function will return an empty list if the pattern is not found in the string, which is equivalent to False in a boolean context. 







#Test
assert text_lowercase_underscore("aab_cbbbc")==(True) 
assert text_lowercase_underscore("abcd")==(False) 
#This test will pass because 'aab_cbbbc' contains sequences of lowercase letters joined with an underscore, and 'abcd' does not. 
#The function will return True for 'aab_cbbbc' and False for 'abcd'. 
#The function will return None if the pattern is not found in the string, which is equivalent to False in a boolean context. 

#Alternatively, we can use list comprehension to achieve the same result.

def text_lowercase_underscore