
def check_element(lst, el):
    return all(x == el for x in lst)

print(check_element(["green", "orange", "black", "white"],'blue')) # False

