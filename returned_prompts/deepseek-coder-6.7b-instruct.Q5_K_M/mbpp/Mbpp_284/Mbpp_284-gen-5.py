def check_element(lst, ele):
    return all(e == ele for e in lst)

print(check_element(["green", "orange", "black", "white"],'blue')) # False

