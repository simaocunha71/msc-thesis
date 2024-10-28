def check_element(lst, element):
    return all(x == element for x in lst)  # Using built-in all() function and generator expression
    # or
    # return len(set(lst)) == 1 and lst[0] == element  # Using set() function to check for uniqueness and list indexing
    # or
    # for i in lst:
    #     if i != element:
    #         return False
    # return True  # Using a for loop to check each element in the list
    # or
    # return lst.count(element) == len(lst)  # Using count() function to check for frequency of the element in the list
    # or
    # return all(x == element for x in lst) and len(set(lst)) == 1  # Using both all() and set() functions
    # or
    # return len([x for x in lst if x != element]) == 0  # Using list comprehension to filter out elements that are not equal to the given element and then check its length
    # or
    # return lst.count(element) == len(lst) and all(x == element for x in lst)  # Using count() function to check for frequency of the element in the list and all() function to check for equality
    # or
    # return len(lst) == 1 or lst.count(element) == len(lst)  # Using count() function to check for frequency of the element in the list and then check its length
    # or
    # return lst[0] == element and len(lst) == 1 or lst.count(element) == len(lst)  # Using list indexing to check the first element and then count() function to check for frequency of the element in the list
    # or
    # return len(lst) == 1 or lst[0] == element  # Using list indexing to check the first element and then check its length
    # or
    # return len(lst) == 1 or all(x == element for x in lst)  # Using all() function to check for equality and then check its length
    # or
    # return len(lst) == 1 or lst[0] == element and all(x == element for x in lst)  # Using list indexing to check the first element, all() function to check for equality and then check its length
    # or
    # return len(lst) == 1 or