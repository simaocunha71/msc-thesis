def check_element(lst: list, element: str) -> bool:
    return all(item == element for item in lst)