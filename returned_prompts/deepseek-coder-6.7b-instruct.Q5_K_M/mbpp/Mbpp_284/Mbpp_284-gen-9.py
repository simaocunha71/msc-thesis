def check_element(lst, elem):
    return all(i == elem for i in lst)

print(check_element(["green", "orange", "black", "white"],'blue')) # False

# Alternative solution
def check_element(lst, elem):
    for i in lst:
        if i != elem:
            return False
    return True

print(check_element(["green", "orange", "black", "white"],'blue')) # False

