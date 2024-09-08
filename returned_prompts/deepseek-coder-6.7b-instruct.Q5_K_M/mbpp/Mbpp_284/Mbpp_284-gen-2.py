def check_element(lst, elm):
    return all(el == elm for el in lst)

print(check_element(["green", "orange", "black", "white"],'blue')) # False


"""
