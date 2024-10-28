def remove_all_spaces(s):
    return s.replace(' ', '')

assert remove_all_spaces('python  program')==('pythonprogram')  # passes
print(remove_all_spaces('python  program'))  # prints 'pythonprogram'  # prints
print(remove_all_spaces('   hello  world  '))  # prints 'helloworld'  # prints

# test
print(remove_all_spaces('   hello  world  '))  # prints 'helloworld'  # prints
print(remove_all_spaces('  This  is  a  test  '))  # prints 'Thisisatest'  # prints
print(remove_all_spaces('  test  string  with  spaces  '))  # prints 'teststringwithspaces'  # prints
print(remove_all_spaces('  this  is  a  test  '))  # prints 'thisisatest'  # prints
print(remove_all_spaces(''))  # prints ''  # prints
print(remove_all_spaces('   '))  # prints ''  # prints
print(remove_all_spaces('  '))  # prints ''  # prints
print(remove_all_spaces('  a  '))  # prints 'a'  # prints
print(remove_all_spaces('  a'))  # prints 'a'  # prints
print(remove_all_spaces('  a  b  c  '))  # prints 'abc'  # prints
print(remove_all_spaces('  a  b  c'))  # prints 'abc'  # prints
print(remove_all_spaces('  a  b'))  # prints 'ab'  # prints
print(remove_all_spaces('  a  b  c  d  '))  # prints 'abcd'  # prints
print(remove_all_spaces('  a  b  c  d'))  # prints 'abcd'  # prints
print(remove_all_spaces('  a  b  c  d  e  '))  # prints 'abcde'  # prints
print(remove_all_spaces('  a  b  c  d  e'))  # prints 'abcde'  # prints
print(remove_all_spaces('  a  b  c  d  e  f  '))  # prints 'abcdef'  # prints
print(remove_all_spaces('  a  b  c  d  e  f'))  # prints 'abcdef'  # prints
print(remove_all_spaces('  a  b  c  d 