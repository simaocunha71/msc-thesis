def check_occurences(tup_list: list) -> dict:
    return {tup: tup_list.count(tup) for tup in tup_list}


