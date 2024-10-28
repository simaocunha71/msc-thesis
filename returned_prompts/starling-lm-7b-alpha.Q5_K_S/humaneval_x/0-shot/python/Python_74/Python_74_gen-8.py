# Python program to find the list with total
# number of chars less than the other

# Function to find total number of characters
# in a string
def total_chars(str_list):
    return sum([len(i) for i in str_list])

# Function to find list with total
# number of characters less than the other
def total_match(str_list1, str_list2):
    if total_chars(str_list1) > total_chars(str_list2):
        return str_list2
    else:
        return str_list1

# Driver program
if __name__ == "__main__":
    # List 1
    lst1 = ['hi', 'admin']
    # List 2
    lst2 = ['hI', 'Hi']
    print(total_match(lst1, lst2))

    # List 1
    lst1 = ['hi', 'admin']
    # List 2
    lst2 = ['hi', 'hi', 'admin', 'project']
    print(total_match(lst1, lst2))

    # List 1
    lst1 = ['hi', 'admin']
    # List 2
    lst2 = ['hI', 'hi', 'hi']
    print(total_match(lst1, lst2))

    # List 1
    lst1 = ['4']
    # List 2
    lst2 = ['1', '2', '3', '4', '5']
    print(total_match(lst1, lst2))





























```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
``