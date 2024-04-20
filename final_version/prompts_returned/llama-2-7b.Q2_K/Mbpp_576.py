"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
import math
def is_Sub_Array(array1,array2):
  
  if len(array1) !=len(array2):
    print("Size of Arrays Does not Match")
    return True
  else:
    for i in range (0, len(array1)):
      a1=array1[i]
      a2=array2[i]
      if abs(a1-a2)>abs((max(array1))-(min(array1)))/4*4 :
        print("Sub Array Does Not Exist")
        return True
      else:
        array1.remove(a1)
        array2.remove(a2)
    return False
print("Hello World!")