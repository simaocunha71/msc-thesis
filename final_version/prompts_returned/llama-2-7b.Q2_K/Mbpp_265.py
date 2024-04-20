"""
Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

def list_split(mylist, n):
    mylist.append('[]') # this is to add an empty [].
    i=0;j=0
    while j<len(mylist)-1:
        if i==n-1 or (i%n)==0 : 
            print("start of list")
            mylist[j+1] = list_split([x for x in mylist[j+1:len(mylist)-2]], n) # splitting the list.
        i+=1; j+=1
    return mylist[0:-1]
