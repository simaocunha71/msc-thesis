from typing import Tuple
def check_type(tup: Tuple) -> bool:
    return all(isinstance(i, type(tup[0])) for i in tup)