def same_len_str(lst):
    return [x for x in lst if len(x)==len(max(lst, key=len))]

# Test
assert same_len_str(["cat","dog","elephant"])==