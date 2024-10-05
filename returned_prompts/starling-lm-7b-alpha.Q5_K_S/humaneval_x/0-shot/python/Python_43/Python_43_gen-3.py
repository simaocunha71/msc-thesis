    #corner case
    if len(l) < 2:
        return False
    #first, create a dictionary to store the count of each element
    count_dict = {}
    for num in l:
        count_dict[num] = count_dict.get(num, 0) + 1
    #then, iterate through each element, if the element is zero, check if there is a pair with it
    for num in l:
        if num == 0:
            if count_dict[num] >= 2:
                return True
        else:
            complement = -num
            if complement in count_dict:
                if count_dict[num] >= 1 and count_dict[complement] >= 1:
                    return True
    return False


























```

```

```