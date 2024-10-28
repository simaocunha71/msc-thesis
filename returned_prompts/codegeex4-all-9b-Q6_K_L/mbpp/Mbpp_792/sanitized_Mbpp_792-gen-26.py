def count_list(test_list: list) -> int:
    count = 0
    for i in test_list:
        if isinstance(i, list):
            count += 1
    return count