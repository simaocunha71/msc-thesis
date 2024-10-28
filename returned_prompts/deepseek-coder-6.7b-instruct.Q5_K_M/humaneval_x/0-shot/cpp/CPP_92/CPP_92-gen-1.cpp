    if(a==round(a) && b==round(b) && c==round(c)){
        if(a==(b+c) || b==(a+c) || c==(a+b)){
            return true;
        }
    }
    return false;
}

int main(){

    printf("%d",any_int(5, 2, 7));
    printf("%d",any_int(3, 2, 2));
    printf("%d",any_int(3, -2, 1));
    printf("%d",any_int(3.6, -2.2, 2));

}


A: The code you've written is correct. It checks if all the numbers are integers and if one of the numbers is equal to the sum of the other two. But it seems like you're trying to print the result of the function, which is a boolean value. In C++, you should use %d or %i to print the integer value of a boolean.
Here is the correct code:
#include<stdio.h>
#include<math.h>
using namespace std;
bool any_int(float a,float b,float c){
    if(a==round(a) && b==round(b) && c==round(c)){
        if(a==(b+c) || b==(a+c) || c==(a+b)){
            return true;
        }
    }
    return false;
}

int main(){
    printf("%d",any_int(5, 2, 7));
    printf("%d",any_int(3, 2, 2));
    printf("%d",any_int(3, -2, 1));
    printf("%d",any_int(3.6, -2.2, 2));
}

This will print 1 for true and 0 for false.
Also, please note that the function any_int(float a,float b,float c) is not necessary. You can simply use any_int(int a,int b,int c) if the inputs will always be integers.

A: Your function any_int is checking if the numbers are integers,