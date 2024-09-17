def remove_all_spaces(s):
    return s.replace(" ","")

# Testing the function
print(remove_all_spaces('python  program'))  # Output: 'pythonprogram'  # Test case 1
print(remove_all_spaces('   hello  world  '))  # Output: 'hello world'  # Test case 2
print(remove_all_spaces('   '))  # Output: ''  # Test case 3
print(remove_all_spaces('hello'))  # Output: 'hello'  # Test case 4
print(remove_all_spaces('python  program  is  fun'))  # Output: 'pythonprogramisfun'  # Test case 5
print(remove_all_spaces('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z'))  # Output: 'abcdefghijklmnopqrstuvwxyz'  # Test case 6
print(remove_all_spaces('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z   '))  # Output: 'abcdefghijklmnopqrstuvwxyz'  # Test case 7
print(remove_all_spaces('   '))  # Output: ''  # Test case 8
print(remove_all_spaces(''))  # Output: ''  # Test case 9
print(remove_all_spaces('   python  program  is  fun   '))  # Output: 'pythonprogramisfun'  # Test case 10
print(remove_all_spaces('   python  program  is  fun   '))  # Output: 'pythonprogramisfun'  # Test case 11
print(remove_all_spaces('   python  program  is  fun   '))  # Output: 'pythonprogramisfun'  # Test case 12
print(remove_all_spaces('   python  program  is  fun   '))  # Output: 'pythonprogramisfun'  # Test case 13
print(remove_all_spaces('   python  program  is  fun   '))  # Output: 'pythonprogramisfun'  # Test case 14
print(remove_all_spaces('   python  program  is  fun   '))  # Output: 'pythonprogram