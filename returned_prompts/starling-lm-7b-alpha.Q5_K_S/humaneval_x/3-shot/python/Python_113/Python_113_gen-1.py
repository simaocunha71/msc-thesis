    def count_odd(s):
        count = 0
        for c in s:
            if int(c) % 2 != 0:
                count += 1
        return f"the number of odd elements {count}n the str{len(s)}ng {len(s)} of the {len(s)}nput."

    return [count_odd(s) for s in lst]


