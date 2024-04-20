"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""

def remove_Occ(str,ch):
    """ 
       Removes the first occurance of "ch" in str which is called for loop
     """
    ch = [x[0] for x in str.split(ch)] #splits it into a list
   ch1 = ""+ch[0]+"" if ch[0] else ch

  result_str = ""
    i=0
for item in ch:
      if i==len(str)-1:
        break;
       i+=1
result_str += str[:i] +" "+ str[i:]
return result_str
print("remove_Occ(\""+str+"\","l") : " )
