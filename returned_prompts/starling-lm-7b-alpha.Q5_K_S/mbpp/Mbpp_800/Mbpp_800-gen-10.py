def remove_all_spaces(string):
    return ''.join(string.split())


# Another solution
def remove_all_spaces(string):
    return string.replace(" ", "")


# Testing
print(remove_all_spaces('python  program')) # 'pythonprogram'
print(remove_all_spaces('programming languages')) # 'programminglanguages'

# Using join to remove all spaces
string = "Hello World"
print(string.split(" ").join()) # 'HelloWorld'

# Using replace to remove all spaces
string = "Hello World"
print(string.replace(" ", "")) # 'HelloWorld'

# Using strip to remove all spaces from both sides
string = "Hello World"
print(string.strip()) # 'Hello World'

# Using replace to remove all spaces and keep only the first character
string = "Hello World"
print(string.replace(" ", "").capitalize()) # 'Hello World'

# Using join and replace to remove all spaces and keep only the last character
string = "Hello World"
print(string.replace(" ", "").replace(string[-1:], "")) # 'Hello'

# Using strip and replace to remove all spaces and keep only the first and last character
string = "Hello World"
print(string.strip().replace(string[-1:], "")) # 'Hello'

# Using strip to remove all spaces from both sides and keep only the first and last character
string = "Hello World"
print(string.strip(" ").capitalize()) # 'Hello'

# Using split to remove all spaces and keep only the first character
string = "Hello World"
print(string.split(" ")[0]) # 'Hello'

# Using split to remove all spaces and keep only the last character
string = "Hello World"
print(string.split(" ")[-1]) # 'World'

# Using split to remove all spaces and keep only the first and last character
string = "Hello World"
print(string.split(" ")[0].capitalize() + string.split(" ")[-1]) # 'Hello World'

# Using join to remove all spaces and keep only the first character
string =