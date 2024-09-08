def find_sum(lst):
    non_repeat = set()
    repeat = set()

    for num in lst:
        if num not in non_repeat:
            non_repeat.add(num)
        else:
            repeat.add(num)

    return sum(non_repeat - repeat)