def diff_even_odd(my_list):
    # find the first even number
    for i in my_list:
        if i%2==0:
            even=i
            break
    # find the first odd number
    for i in my_list:
        if i%2!=0:
            odd=i
            break
    return even-odd
