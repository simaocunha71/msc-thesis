    return [f"the number of odd elements {count}n the str{idx}ng {idx} of the {idx}nput." for idx, s in enumerate(lst) for count in [str(s.count(str(int(d) % 2 != 0))) for d in s]]


