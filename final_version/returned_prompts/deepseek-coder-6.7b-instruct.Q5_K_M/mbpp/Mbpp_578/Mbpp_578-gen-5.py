def interleave_lists(lst1, lst2, lst3):
    interleaved = []
    for i in range(len(lst1)):
        interleaved.append(lst1[i])
        interleaved.append(lst2[i])
        interleaved.append(lst3[i])
    return interleaved

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))

"""
Output:
[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""
<jupyter_output>
[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
<jupyter_text>
