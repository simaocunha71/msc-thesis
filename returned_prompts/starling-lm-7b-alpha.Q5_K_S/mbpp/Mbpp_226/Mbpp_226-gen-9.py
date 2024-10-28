
def odd_values_string(s: str) -> str:
    odd_index = [i for i in range(len(s)) if i % 2 != 0]
    odd_values = [s[i] for i in odd_index]
    return ''.join(odd_values)


