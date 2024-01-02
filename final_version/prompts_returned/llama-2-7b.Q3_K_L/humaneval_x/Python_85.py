
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    res = []
    for i in range(len(lst), -1 , -1):
        if lst[i] % 2 == 0 and len(res) < 3: # check for empty list
            print(lst[i])
            res.append(lst[i])
    return res

if __name__=='__main__':
     print(add([4, 1]))