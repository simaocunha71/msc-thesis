def issort_list(list_):
    return all(list_[i] <= list_[i + 1] for i in range(len(list_) - 1))