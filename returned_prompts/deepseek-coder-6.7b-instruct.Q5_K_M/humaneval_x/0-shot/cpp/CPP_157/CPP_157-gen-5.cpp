    //Your code here
    float temp;
    if(a > b && a > c){
        temp = a;
        a = c;
        c = temp;
    }
    else if(b > a && b > c){
        temp = b;
        b = c;
        c = temp;
    }

    if(c*c == a*a + b*b)
        return true;
    else
        return false;
}
int main(){
    printf("%d",right_angle_triangle(3,4,5));
    printf("%d",right_angle_triangle(1,2,3));
    return 0;
}
*/


A: You can use the Pythagorean theorem to check if a triangle is right-angled. This theorem states that in a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. This can be written as: a² + b² = c² where c is the hypotenuse and a and b are the other two sides.

Here is the Python code:

def right_angle_triangle(a, b, c):
    # sort the sides
    sides = sorted([a, b, c])

    # check if the triangle is right-angled
    return sides[2]**2 == sides[0]**2 + sides[1]**2

print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False

In this code, we first sort the sides of the triangle in ascending order. Then we check if the square of the largest side (hypotenuse, c) is equal to the sum of the squares of the other two sides (a and b). If it is, then the triangle is right-angled and the function returns True. Otherwise, it returns False.

Please note that this code assumes that the inputs are valid lengths of a triangle. If the inputs are not valid lengths of a triangle, the function may return incorrect results.

Also, note that this code uses Python's sorted function to sort the sides. This function returns a new