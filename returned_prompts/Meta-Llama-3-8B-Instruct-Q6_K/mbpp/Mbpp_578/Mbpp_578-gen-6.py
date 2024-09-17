def interleave_lists(list1, list2, list3):
    return [x for group in zip(list1, list2, list3) for x in group]
# test the function
print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))


# This function works by using the built-in zip function, which pairs up elements from the input lists. The result is a list of tuples, where each tuple contains one element from each input list. The list comprehension then flattens this list of tuples into a single list. The result is a list where elements from the three input lists are interleaved.
# For example, if you call the function with the lists [1,2,3,4,5,6,7], [10,20,30,40,50,60,70], and [100,200,300,400,500,600,700], it will return the list [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700].
# The unit test provided in the problem statement verifies that this function behaves as expected. It checks that the function returns the correct result when called with the lists [1,2,3,4,5,6,7], [10,20,30,40,50,60,70], and [100,200,300,400,500,600,700]. The expected result is a list where elements from these lists are interleaved. The function is tested by comparing the result it returns with the expected result. If the result is correct, the test passes; otherwise, it fails.