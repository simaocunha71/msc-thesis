def move_num(s):
    num_list = [i for i in s if i.isdigit()]
    str_list = [i for i in s if not i.isdigit()]
    return ''.join(str_list + num_list)

print(move_num('I1love143you55three3000thousand'))  # Iloveyouthreethousand1143553000

# 2. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

