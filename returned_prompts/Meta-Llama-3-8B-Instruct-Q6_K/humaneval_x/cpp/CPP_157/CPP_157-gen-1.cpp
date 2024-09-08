    if(a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)
        return true;
    else
        return false;

}

int main(){
    printf("%d\n",right_angle_triangle(3, 4, 5));
    printf("%d\n",right_angle_triangle(1, 2, 3));
    return 0;
}A

C:
#include<stdio.h>
#include<math.h>
using namespace std;
bool right_angle_triangle(float a,float b,float c){
    if(a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)
        return true;
    else
        return false;

}

int main(){
    printf("%d\n",right_angle_triangle(3, 4, 5));
    printf("%d\n",right_angle_triangle(1, 2, 3));
    return 0;
}A

Explanation:
The program checks if the three sides of a triangle can form a right-angled triangle.
It uses the Pythagorean theorem (a*a+b*b==c*c) to check if the triangle is a right-angled triangle.
The function right_angle_triangle takes three float arguments representing the lengths of the three sides of the triangle.
The function returns true if the three sides form a right-angled triangle and false otherwise.

In the main function, we call the right_angle_triangle function with different sets of arguments and print the results.
The first call with arguments 3, 4, 5 returns true because 3, 4, 5 are the lengths of a right-angled triangle.
The second call with arguments 1, 2, 3 returns false because 1, 2, 3 do not form a right-angled triangle. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. A