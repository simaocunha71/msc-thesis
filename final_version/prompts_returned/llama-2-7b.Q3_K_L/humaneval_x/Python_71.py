
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    
    if a + b > c or a + c > b or b+c > a:
        return -1
        
    else:
       area = float(a*b)/2
       return round(area,2)

print("Triangle Area Calculator")
answer=input("Enter A side: ")
try:
    answer=float(answer)
except ValueError:
    print("please enter numbers")
else:
    if answer > 0:
        print("Invalid Input!")
        print("Please re-enter value of A: ")
        answer = input("Enter A side again: ")
        try:
            answer=float(answer)
        except ValueError:
            print("please enter numbers")
    else:
        if area_func(answer,triangle_area):
            print("Triangle Area Calculator 2 decimal points: ",area_func(answer,triangle_area))
            break
    
        
else:
    if answer >0 and area_func(answer,triangle_area):
        print("Triangle Area Calculator 2 decimal points",area_func(answer,triangle_area) )
    else:
        print("Invalid Input!")