
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''

    a = int(a)
    
    # if(a==0):
    # 	return True
  
    # elif(a>0 and a<9):
    # 	if(a == 2 or a==4 or a==8 or a==16 or a==32 or a==64):
    # 		return True
    # else:
    # 	return False
    
    if isinstance(a, int) and a >= 0 and (a == 1 or a == -1 or (a % 2 == 0)):
        return True
    else:
        return False