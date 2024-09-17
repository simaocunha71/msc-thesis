def tup_string(t):
    return ''.join(t).replace(',', '').replace('\'', '').replace('(', '').replace(')', '').replace(' ', '')

# Testing
print(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))) # Should print: "exercises"
print(tup_string(('a', 'b', 'c'))) # Should print: "abc" 
print(tup_string((1, 2, 3))) # Should print: "123" 
print(tup_string((True, False, True))) # Should print: "TrueFalseTrue" 
print(tup_string(('a', 'b', 'c'), ' ')) # Should print: "a b c" 
print(tup_string(('a', 'b', 'c'), ',')) # Should print: "a,b,c" 
print(tup_string(('a', 'b', 'c'), 'x')) # Should print: "axbxc" 

# Testing with None
print(tup_string(None)) # Should print: "None" 

# Testing with empty tuple
print(tup_string(())) # Should print: "" 
print(tup_string(('',))) # Should print: "" 
print(tup_string(('a',),)) # Should print: "a" 
print(tup_string(('a',), ' ')) # Should print: "a" 
print(tup_string(('a',), ', ')) # Should print: "a"  # Testing with empty strings
print(tup_string(('',))) # Should print: "" 
print(tup_string(('a', '', 'c'))) # Should print: "a" 
print(tup_string(('a', '', 'c'), ' ')) # Should print: "a" 
print(tup_string(('a', '', 'c'), ',')) # Should print: "a" 
print(tup_string(('a', '', 'c'), 'x')) # Should print: "ax" 
print(tup_string(('', '', ''))) # Should print: "" 
print(tup_string(('', '', ''), ' ')) # Should print: "" 
print(tup_string(('', '', ''), ',')) # Should print: "" 
print(tup_string(('', '', ''), 'x')) # Should print: "" 
# Testing with mixed types
print(tup_string((1, 'a', True, 3.5,