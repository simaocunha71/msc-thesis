from typing import List, Tuple
def start_withp(words: List[str]) -> Tuple[str, str]:
    return [word for word in words if word.startswith('p')][:2]