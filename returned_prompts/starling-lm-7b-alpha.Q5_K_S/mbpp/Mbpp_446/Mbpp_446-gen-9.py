def count_Occurrence(tup,list):
    cnt=0
    for i in tup:
        if i in list:
            cnt+=list.count(i)
    return cnt

# Driver Code
print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']))







"""
The time complexity of the above program is O(n+m) because in the for loop, we are traversing the tuple and list of size n and m respectively. Here m is the number of elements in the list and n is the number of elements in the tuple.

The space complexity of the above program is O(1) because it only uses a single integer variable 'cnt' to store the count of the occurrence of an element in the tuple.

"""



"""
In this program, we are calculating the count of occurrence of all the elements of the tuple in the list. Here, we are using a for loop to iterate through the tuple and check each element if it is present in the list using the 'in' keyword. If the element is present in the list, then we use the count() method to count the number of occurrences of that element in the list and add it to the 'cnt' variable. Finally, we return the 'cnt' variable which contains the total count of occurrence of all the elements of the tuple in the list.
"""



"""
The time complexity of the above program is O(n+m) because in the for loop, we are traversing the tuple and list of size n and m respectively. Here m is the number of elements in the list and n is the number of elements in the tuple. In the worst case, we may have to traverse all the elements of the tuple and list, hence the time complexity becomes O(n+m).

The space complexity of the above program is O(1) because it only uses a single integer variable 'cnt' to store the count of the occurrence of an element in the tuple. Hence, the space complexity becomes O(1).
"""



"""
In this program, we are calculating the count of occurrence of all the elements of the tuple in the list. Here, we are using a for loop to iterate through the tuple and