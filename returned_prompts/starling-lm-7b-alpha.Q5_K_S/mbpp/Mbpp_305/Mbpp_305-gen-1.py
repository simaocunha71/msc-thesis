"""
def start_withp(words):
    return [word for word in words if word.startswith('p')][:2]

"""
from typing import List, Tuple

def start_withp(words: List[str]) -> Tuple[str, str]:
    return [word for word in words if word.startswith('p')][:2]


# start_withp(["Python PHP", "Java JavaScript", "c c++"])
# Python    PHP

# start_withp(["Python Python", "Java JavaScript", "c c++"])
# Python    Python

# start_withp(["Python PHP", "Java JavaScript", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP

# start_withp(["Python PHP", "Java", "c++"])
# Python    PHP


def start_withp(words: List[str]) -> Tuple[str, str]:
    return [word for word in words if word.startswith('p')][:2]


# start_withp(["Python PHP", "Java JavaScript", "c c++"])
# ('Python', 'PHP')

# start_withp(["Python PHP", "Java JavaScript",