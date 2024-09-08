def check_element(lst, elem):
    return all(i == elem for i in lst)

print(check_element(["green", "orange", "black", "white"], 'blue'))  # False


