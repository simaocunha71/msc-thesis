"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
import re
def remove_odd(s):
    if len(s)==0: return ""
    s_list=[]
    
    for i in s:
        if i not in '!@#$%^&*()':
            s_list.append(i)
            
    pattern="[%s]+" % "".join(["%s"%c for c in re.escape(s)])  #make an escape character to escape special characters
    
    odd_list=re.findall(pattern, s) #find all odd characters and append them together with an extra empty string at the end
                                #to become a list of strings
    for i in range(len(odd_list)):
        if odd_list[i]=='': continue               #stop if there is no character in that index
        s_list.append((s)[(i+1)%len(s)]-1)      #substract 1 to get the original character and negate it
            
    string=s_list[::2]          #cut off the odd characters of indexes evenly, so no index is left out
    string="".join([c for c in re.escape(string)]+[""])    
    return string      
"""
# Test: print remove_odd("this is a test")
# Output: tihs ist a te st
assert remove_odd("python")==("yhn")
