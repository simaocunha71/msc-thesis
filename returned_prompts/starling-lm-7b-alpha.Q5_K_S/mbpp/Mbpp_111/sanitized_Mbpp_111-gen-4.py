def common_in_nested_lists(lists):
    set_ = set()
    for l in lists:
        for i in l:
            set_.add(i)
    return set_