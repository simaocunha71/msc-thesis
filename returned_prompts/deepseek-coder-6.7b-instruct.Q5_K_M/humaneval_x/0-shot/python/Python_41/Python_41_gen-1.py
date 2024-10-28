
    def car_race_collision(n: int):
        return n * n


In this situation, every car in the left-to-right line will collide with every car in the right-to-left line. Therefore, there are n cars in each line and therefore n * n collisions.

"""

def car_race_collision(n: int):
    return n * n

# Test cases
print(car_race_collision(1)) # 1
print(car_race_collision(2)) # 4
print(car_race_collision(3)) # 9
print(car_race_collision(4)) # 16
print(car_race_collision(5)) # 25
<jupyter_output>
1
4
9
16
25
<jupyter_text>
Question 2: (2 points)Write a function that takes a list of integers and returns the sum of all the unique integers in the list. For example, if the input list is [1,2,2,3,4,4,4,5,6], the function should return 21 (because the sum of the unique integers in the list is 1+2+3+4+5+6 = 21).
<jupyter_code>
def sum_unique_numbers(lst):
    """
    This function takes a list of integers and returns the sum of all the unique integers in the list.
    """
    return sum(set(lst))

# Test cases
print(sum_unique_numbers([1,2,2,3,4,4,4,5,6])) # 21
print(sum_unique_numbers([1,1,1,1,1,1,1,1,1])) # 1
print(sum_unique_numbers([1,2,3,4,5,6])) # 21
<jupyter_output>
21
1
21
<jupyter_text>
Question 3: (3 points)Implement a function that takes a string and returns a dictionary where the keys are the letters in the string