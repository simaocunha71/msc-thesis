We are given the lengths of the three sides of a triangle. To find out if the triangle is a right-angled triangle, we need to rearrange the lengths of the sides so that one of the sides is the hypotenuse (c).

B:
After rearranging, we check if a^2 + b^2 = c^2, if true then the triangle is a right-angled triangle.

*/

// Code:
/*
bool right_angle_triangle(float a,float b,float c){

    float temp;
    if(a>b && a>c){
        temp = a;
        a = c;
        c = temp;
    }
    else if(b>a && b>c){
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
    printf("%d\n",right_angle_triangle(3,4,5));
    printf("%d\n",right_angle_triangle(1,2,3));
    return 0;
}
*/

//