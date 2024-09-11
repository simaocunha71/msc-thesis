def reverse_string_list(string_list):
    '''
    Parameters:
        string_list (list): list of strings
    Returns:
        list: list of reversed strings
    '''
    return [s[::-1] for s in string_list]

# Testing
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
print("All tests passed")






# Here is the Python code to reverse each string in a given list of string values

def reverse_string_list(string_list):
    '''
    Parameters:
        string_list (list): list of strings
    Returns:
        list: list of reversed strings
    '''
    return [s[::-1] for s in string_list]
```