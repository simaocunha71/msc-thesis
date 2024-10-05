from typing import List


def all_prefixes(string: str) -> List[str]:
    return [string[0:i] for i in range(1, len(string) + 1)]
