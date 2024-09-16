def median_numbers(a,b,c):
    sorted_list = sorted([a,b,c])
    if sorted_list[1]==sorted_list[2]:
        return sorted_list[1]
    else:
        return (sorted_list[1]+sorted_list[2])/2




