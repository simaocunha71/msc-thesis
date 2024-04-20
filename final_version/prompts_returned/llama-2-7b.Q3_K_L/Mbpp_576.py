"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""

def is_Sub_Array(arr1, arr2):
  if arr1 == []:
    return True;
  elif arr1[0] != arr2[0]:
      return False;
  else:
    for i in range(len(arr1)):
      if arr2[i] not in arr1 or len(arr1[i]) < len(arr2):
        return False;
      elif (not arr1[i][-1] == arr2[i][0] and arr1[i][-1] != -1) and (not arr1[i][-1] == arr2[i][-1]) :
        if len(arr1[i]) < len(arr2):
          return False;
      else:
        return True;
