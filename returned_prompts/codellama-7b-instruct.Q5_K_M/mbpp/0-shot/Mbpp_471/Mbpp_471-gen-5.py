def find_remainder(my_list,n):
    #write your code here
    return (reduce(lambda x,y: (x*y)%n,my_list,1))

