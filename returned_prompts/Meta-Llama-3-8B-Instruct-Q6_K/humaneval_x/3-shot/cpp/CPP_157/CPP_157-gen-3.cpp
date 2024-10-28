    if (a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)
    return true;
    else
    return false;
}
//or
#include<stdio.h>
#include<math.h>
using namespace std;
bool right_angle_triangle(float a,float b,float c){
    if (a*a+b*b>c*c || a*a+c*c>b*b || b*b+c*c>a*a)
    return false;
    else
    return true;
} //both are correct
// The first one checks if the sum of the squares of the two shorter sides is equal to the square of the longest side. If so, the triangle is right-angled. The second one checks if any two sides are longer than the third side. If so, the triangle is not right-angled. If none of these conditions are met, the triangle is right-angled. This is because the Pythagorean theorem states that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides. Therefore, if the sum of the squares of the two shorter sides is equal to the square of the longest side, the triangle is right-angled. Otherwise, it is not. The second method is more efficient and easier to understand.