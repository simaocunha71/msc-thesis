    //sorting the sides
    if(a > b && a > c){
        if(pow(a,2) == pow(b,2) + pow(c,2))
            return true;
    }
    else if(b > a && b > c){
        if(pow(b,2) == pow(a,2) + pow(c,2))
            return true;
    }
    else if(c > a && c > b){
        if(pow(c,2) == pow(a,2) + pow(b,2))
            return true;
    }
    else
        return false;
}

int main(){
    printf("%d\n",right_angle_triangle(3, 4, 5));
    printf("%d\n",right_angle_triangle(1, 2, 3));
    return 0;
}

*/

#include<stdio.h>
#include<stdbool.h>

bool right_angle_triangle(int a,int b,int c){

    int max,squareSum;
    //sorting the sides
    if(a > b && a > c){
        max = a;
        squareSum = b*b + c*c;
    }
    else if(b > a && b > c){
        max = b;
        squareSum = a*a + c*c;
    }
    else{
        max = c;
        squareSum = a*a + b*b;
    }

    if(max*max == squareSum)
        return true;
    else
        return false;
}

int main(){
    printf("%d\n",right_angle_triangle(3, 4, 5));
    printf("%d\n",right_angle_triangle(1, 2, 3));
    return 0;
}

/*
