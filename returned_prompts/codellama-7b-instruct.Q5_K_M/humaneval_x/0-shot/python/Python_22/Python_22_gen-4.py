from typing import List, Any, cast


def filter_integers(values: List[Any]) -> List[int]:
    return [cast(int, value) for value in values if isinstance(value, int)]