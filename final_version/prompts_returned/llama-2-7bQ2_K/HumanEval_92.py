
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''

    # Write your code here
    if (x == x + y) and (y == z):
        print("True")

    elif ((x != (x+y)) or (y!=z)):
        print("False")

def any_num(x, y, z):
    ''' 
    Create a function that takes 3 numbers. Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers. Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
        
    any_num(-10, -8, 6) ➞ False
      
    '''
    if (x == x + y) and (y==z):
        print("True")
    
    elif ((x != (x+y)) or (y!=z)):
        print("False")
        
def test_main():
    print("any_int()")
    print(any_int(1, 2, 3))
    print('any_num()')
    print(any_num(-10, -8,6) )    
test_main()

