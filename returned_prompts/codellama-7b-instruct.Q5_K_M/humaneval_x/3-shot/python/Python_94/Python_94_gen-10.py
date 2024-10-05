    lst_prime = [x for x in lst if is_prime(x)]
    if lst_prime:
        return sum(map(int, str(max(lst_prime))))
    else:
        return 0


