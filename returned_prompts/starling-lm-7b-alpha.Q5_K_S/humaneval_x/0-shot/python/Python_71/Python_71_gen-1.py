    # Given three sides of a triangle, return the area rounded to 2 decimal points, if the three sides form a valid triangle. Otherwise return -1. 
    # Three sides make a valid triangle when the sum of any two sides is greater than the third side. 

    # Your code here
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return "{:.2f}".format(area)
    else:
        return -1





def test_triangle_area():
    assert triangle_area(3, 4, 5) == 6.00, "First example failed"
    assert triangle_area(1, 2, 10) == -1, "Second example failed"
    assert triangle_area(10, 20, 30) == -1, "Third example failed"
    assert triangle_area(7, 24, 25) == 30.00, "Fourth example failed"
    assert triangle_area(12, 15, 19) == 30.00, "Fifth example failed"
    print("All test cases passed")

test_triangle_area()






# Here are some example test cases to help you get started:

# >>> triangle_area(3, 4, 5) == 6.00
# True
# >>> triangle_area(1, 2, 10) == -1
# True
# >>> triangle_area(10, 20, 30) == -1
# True
# >>> triangle_area(7, 24, 25) == 30.00
# True
# >>> triangle_area(12, 15, 19) == 30.00
# True
# >>> triangle_area(1, 2, 3) == -1
# True
# >>> triangle_area(1, 2, 4) ==