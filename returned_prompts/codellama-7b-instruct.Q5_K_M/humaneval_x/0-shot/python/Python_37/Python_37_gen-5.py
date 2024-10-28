

def sort_even(l: list) -> list:
    l_even = [l[i] for i in range(len(l)) if i % 2 == 0]
    l_even.sort()
    return [l[i] if i % 2 != 0 else l_even[i // 2] for i in range(len(l))]
