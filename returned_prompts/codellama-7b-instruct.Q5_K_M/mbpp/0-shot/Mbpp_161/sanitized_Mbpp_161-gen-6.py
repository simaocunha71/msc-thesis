from typing import List
def remove_elements(original_list: List, elements_to_remove: List) -> List:
    return list(set(original_list) - set(elements_to_remove))