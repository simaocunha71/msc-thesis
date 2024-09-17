def frequency_lists(lists: list) -> dict:
    frequency = {}
    for sublist in lists:
        for element in sublist:
            frequency[element] = frequency.get(element, 0) + 1
    return frequency