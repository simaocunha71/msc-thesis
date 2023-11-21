
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    
    if q == []:
        return False

    f = float(sum(q))
        
    if len(w)==0:
        return len(q)<=5 # max is 5 because there are 10 in the array [3,2,...][9] and no w
    
    for i in range(len(q)):
            q_list = q[i].split(' ')
            p=len(q_list)-1
            while p>=0:
                if p==0:
                    f-=float(w[p])
                else:
                    f+=float(w[p])
                p-=1
    return f < w[:]
    
    
