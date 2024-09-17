def interleave_lists(list1, list2, list3):
    return [x for t in zip(list1, list2, list3) for x in t]

# Test the function
print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))  # [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]




