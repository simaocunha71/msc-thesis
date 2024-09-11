def sum_of_digits(lst):
    return sum(sum(int(i) for i in str(num)) for num in lst)  # or 
    # return sum(int(i) for num in lst for i in str(num))  # or 
    # return sum(map(sum, map(int, map(str, lst))))  # or 
    # return sum(sum(int(i) for i in str(num)) for num in lst) if lst else 0  # or 
    # return sum(int(i) for num in lst for i in str(num)) if lst else 0  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or 
    # return sum(sum(int(i) for i in str(num)) for num in lst) if lst else 0  # or 
    # return sum(int(i) for num in lst for i in str(num)) if lst else 0  # or  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or  # or 
    # return sum(sum(int(i) for i in str(num)) for num in lst) if lst else 0  # or 
    # return sum(int(i) for num in lst for i in str(num)) if lst else 0  # or  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or  # or 
    # return sum(sum(int(i) for i in str(num)) for num in lst) if lst else 0  # or 
    # return sum(int(i) for num in lst for i in str(num)) if lst else 0  # or  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or 
    # return sum(map(sum, map(int, map(str, lst)))) if lst else 0  # or  # or 
    # return sum(sum(int(i) for i in str(num)) for