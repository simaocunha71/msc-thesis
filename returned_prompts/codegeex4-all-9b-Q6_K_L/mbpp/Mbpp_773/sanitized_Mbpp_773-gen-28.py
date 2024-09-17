def occurance_substring(test_str: str, test_sub: str):
    if test_sub in test_str:
        return test_sub, test_str.index(test_sub), test_str.rindex(test_sub)
    else:
        return None