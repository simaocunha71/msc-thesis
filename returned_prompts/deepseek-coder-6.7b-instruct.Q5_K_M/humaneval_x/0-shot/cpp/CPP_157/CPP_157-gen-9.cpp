    float temp;
    //sorting the sides in ascending order
    if(a>b){
        temp=a;
        a=b;
        b=temp;
    }
    if(b>c){
        temp=b;
        b=c;
        c=temp;
    }
    if(a>b){
        temp=a;
        a=b;
        b=temp;
    }

    //checking if it is a right-angled triangle
    if(pow(c,2)==pow(a,2)+pow(b,2))
        return true;
    else
        return false;
}
int main() {
    printf("%d", right_angle_triangle(3, 4, 5));
    printf("%d", right_angle_triangle(1, 2, 3));
    return 0;
}
*/

#include<stdio.h>
#include<math.h>

bool right_angle_triangle(float a,float b,float c){

    float temp;
    //sorting the sides in ascending order
    if(a>b){
        temp=a;
        a=b;
        b=temp;
    }
    if(b>c){
        temp=b;
        b=c;
        c=temp;
    }
    if(a>b){
        temp=a;
        a=b;
        b=temp;
    }

    //checking if it is a right-angled triangle
    if(pow(c,2)==pow(a,2)+pow(b,2))
        return true;
    else
        return false;
}
int main() {
    printf("%d", right_angle_triangle(3, 4, 5));
    printf("%d", right_angle_triangle(1, 2, 3));
    return 0;
}

*/

//