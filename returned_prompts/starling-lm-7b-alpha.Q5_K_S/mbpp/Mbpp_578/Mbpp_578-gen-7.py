"""
def interleave_lists(list_1, list_2, list_3):
    # Initialize a result list
    result = []

    # Initialize pointers for each list
    pointer_1 = 0
    pointer_2 = 0
    pointer_3 = 0

    # Traverse the lists while there are elements left
    while pointer_1 < len(list_1) and pointer_2 < len(list_2) and pointer_3 < len(list_3):
        # Check which element is smaller
        if list_1[pointer_1] < list_2[pointer_2] and list_1[pointer_1] < list_3[pointer_3]:
            result.append(list_1[pointer_1])
            pointer_1 += 1
        elif list_2[pointer_2] < list_1[pointer_1] and list_2[pointer_2] < list_3[pointer_3]:
            result.append(list_2[pointer_2])
            pointer_2 += 1
        else:
            result.append(list_3[pointer_3])
            pointer_3 += 1

    # Append remaining elements of the first list
    while pointer_1 < len(list_1):
        result.append(list_1[pointer_1])
        pointer_1 += 1

    # Append remaining elements of the second list
    while pointer_2 < len(list_2):
        result.append(list_2[pointer_2])
        pointer_2 += 1

    # Append remaining elements of the third list
    while pointer_3 < len(list_3):
        result.append(list_3[pointer_3])
        pointer_3 += 1

    return result

# Testing the function
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 2