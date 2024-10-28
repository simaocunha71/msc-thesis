def issort_list(list_var):
    list_var.sort()
    if list_var==sorted(list_var):
        return True
    else:
        return False