def check_element(lst: list, element) -> bool:
    return all(x == element for x in lst)