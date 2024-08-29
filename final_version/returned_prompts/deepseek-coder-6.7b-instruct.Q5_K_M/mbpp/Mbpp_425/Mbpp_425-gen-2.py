def count_element_in_list(lst, ele):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(ele)
        else:
            if sublist == ele:
                count += 1
    return count

# Test
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)) # Should return 3


"""
