def remove_all_spaces(s):
    return s.replace(" ", "") # or return s.replace(' ', '')

# Test
print(remove_all_spaces('python  program')) # Output: pythonprogram
print(remove_all_spaces('Hello, World!')) # Output: Hello,World!
print(remove_all_spaces('   This   is   a   test   ')) # Output: Thisisatest
print(remove_all_spaces('')) # Output: 
print(remove_all_spaces('No spaces here')) # Output: No spaces here
print(remove_all_spaces('   ')) # Output: 
print(remove_all_spaces('Hello, World! ')) # Output: Hello, World!
print(remove_all_spaces('  ')) # Output: 
print(remove_all_spaces('  Hello, World!')) # Output: Hello, World! 
print(remove_all_spaces('Hello, World!  ')) # Output: Hello, World!
print(remove_all_spaces('  Hello, World!  ')) # Output: Hello, World! 
print(remove_all_spaces('  Hello, World!  Hello, World!')) # Output: Hello, World!Hello, World! 
print(remove_all_spaces('  Hello, World!  Hello, World!  ')) # Output: Hello, World!Hello, World! 
print(remove_all_spaces('  Hello, World!  Hello, World!  Hello, World!')) # Output: Hello, World!Hello, World!Hello, World! 
print(remove_all_spaces('   Hello, World!  Hello, World!  Hello, World!')) # Output: Hello, World!Hello, World!Hello, World! 
print(remove_all_spaces('   Hello, World!  Hello, World!  Hello, World!  ')) # Output: Hello, World!Hello, World!Hello, World! 
print(remove_all_spaces('   Hello, World!  Hello, World!  Hello, World!  Hello, World!')) # Output: Hello, World!Hello, World!Hello, World!Hello, World! 
print(remove_all_spaces('   Hello, World!  Hello, World!  Hello, World!  Hello, World!  ')) # Output: Hello, World!Hello, World!Hello, World!Hello, World! 
print(remove_all_spaces('   Hello, World!  Hello, World!  Hello, World!  Hello, World!  Hello, World!')) # Output: Hello, World!Hello, World