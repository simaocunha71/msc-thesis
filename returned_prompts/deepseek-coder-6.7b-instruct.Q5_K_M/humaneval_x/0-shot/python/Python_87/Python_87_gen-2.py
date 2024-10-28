
def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        for j, item in enumerate(row):
            if item == x:
                coordinates.append((i, j))
    return sorted(coordinates, key=lambda y: (y[0], -y[1]))

print(get_row([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
], 1))  #== [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1))  #== []
print(get_row([[], [1], [1, 2, 3]], 3))  #== [(2, 2)]

#Explanation:
#The function iterates through the given list lst and for each item, 
#it checks if the item is equal to x. If it is, it appends the coordinates 
#of that item to the list coordinates. Then it sorts the list of tuples 
#by first sorting by row (which is the first element of each tuple), and 
#then by column (which is the second element of each tuple), in descending order. 
#It returns this sorted list of tuples.

#Note: 
#The use of lambda in the sort function is to sort by the second element of each tuple in descending order. 
#This is done by prefixing the second element with a "-". 
#The reason for this is that Python's sort function sorts in ascending order by default, 
#but we want to sort in descending order. Hence, by prefixing with "-", we reverse the sort order.
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
[]
[(2, 2)]
<jupyter_text>
Problem 4
<jupyter_code>