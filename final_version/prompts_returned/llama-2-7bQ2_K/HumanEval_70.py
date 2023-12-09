
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    def is_strange(lst):
        if not len(lst) : return True
        elif lst[0][0] > lst[1][0]: # If first entry in list is greater than second entry
            return False
        else:
            return True

    for i in range (len(lst)):
         if is_strange(lst):
             break
    return lst[:i+1].copy()

def test():
    print strange_sort_list([]) # returns []
    print strange_sort_list([5, 2, 3, 4]) #returns [5, 4, 2, 3]
    print strange_sort_list([5, 5, 10, 15, 20, 25, 30, 35, 40, 70]) # returns [5, 10, 70, 25, 60, 55, 45]
    print strange_sort_list([5, 5, 5, 5]) #returns [5, 5, 5, 5] as if the sort is not performed!
    pass
\end{code}

The problem is I dont know how to do my own test cases. I would appreciate any help in this regard. Here are my test cases:
\begin{itemize}
\item [5,2,3] -> [5, 4, 2, 3] because the first element is greater than second so break out of the loop and return [] to indicate no more elements
\item [10,9,8,7]