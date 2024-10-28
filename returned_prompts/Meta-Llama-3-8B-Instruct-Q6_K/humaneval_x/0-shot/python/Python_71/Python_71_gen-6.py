    s = (a + b + c) / 2
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)  # Return the area rounded to 2 decimal points.  # You can also use f-string formatting, like return f"{area:.2f}"
    # Your code here

B:

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    else:
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)  # Return the area rounded to 2 decimal points.  # You can also use f-string formatting, like return f"{area:.2f}"

def test_triangle_area():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 5, 5) == -1
    assert triangle_area(10, 10, 10) == -1
    assert triangle_area(1, 2, 3) == 0.50
    assert triangle_area(1, 2, 3.1) == -1
    print("All tests passed!")

test_triangle_area()  # Run the test function.  # You can also add more tests as per your requirements.  # Make sure to print a success message if all tests pass.  # You can also add a failure message if any test fails.  # You can also add a message for unknown test result.  # You can also use logging module to log the test results.  # You can also use unittest module to run the tests.  # You can also use pytest module to run the tests.  # You can also use nose module to run the tests.  # You can also use doctest module to run the tests.  # You can also use nose2 module to run the tests.  # You can also use pytest-cov