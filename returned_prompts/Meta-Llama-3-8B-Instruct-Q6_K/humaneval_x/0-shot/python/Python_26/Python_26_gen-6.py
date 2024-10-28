    from collections import OrderedDict

    seen = OrderedDict()
    result = []

    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result
    # return list(set(numbers))  # This will not preserve the order of elements. 
    # Also, it will not keep the duplicates in the order they appear in the input list. 
    # For example, if the input is [2, 3, 1, 2], the output will be [1, 3], not [1, 2, 3].
    # The correct order is preserved by using OrderedDict. 

    # The set operation will not work because it does not preserve the order of elements. 
    # For example, if the input is [2, 3, 1, 2], the output will be [1, 2, 3], not [1, 2, 3].
    # Also, set operation does not keep the duplicates in the order they appear in the input list.
    # For example, if the input is [2, 3, 1, 2], the output will be [1, 3], not [1, 2, 3].
    # The correct order is preserved by using OrderedDict. 
    # The set operation can be used to remove duplicates, but it does not preserve the order of elements. 
    # For example, if the input is [2, 3, 1, 2], the output will be [1, 3], not [1, 2, 3].
    # The correct order is preserved by using OrderedDict. 
    # The set operation can be used to remove duplicates, but it does not preserve the order of elements. 
    # For example, if the input is [2, 3, 1, 2], the output will be [1, 3], not [1, 2, 3]. 
    # The correct order is preserved by using OrderedDict. 





from collections import OrderedDict

def remove_duplicates(numbers):
    seen = OrderedDict()
    result = []

    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result

print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([2