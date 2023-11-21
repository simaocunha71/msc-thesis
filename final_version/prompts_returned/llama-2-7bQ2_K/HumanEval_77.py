
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

    # CUBE OF SOME INTEGER
    def get_some_number():
        num = 999
        n = num + 1
        while (n != num):
            if (n%3 == 0 and n %5 == 0) : #cube of some int number
                return True
            else:
                n += 1
            
    iscube(a) == get_some_number()
    

a = int(input("Enter a number: "))
if (iscube(a)):
        print ("It's a cube of some integer")
else:
        print ("It's not a cube of any integer")