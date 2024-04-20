"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
#!/bin/python3

def find_parity(x):
   if x % 2 != 0:
     return True
   else :
      return False

a = int(input("Enter the number for which you want to calculate parity: "))
b = find_Parity(a)
print ("\n", b , "\n")