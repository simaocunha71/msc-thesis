    if((a==b+c) || (b==a+c) || (c==a+b)){
        if((a==round(a)) && (b==round(b)) && (c==round(c))){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        return false;
    }
}

int main(){
    printf("%d\n",any_int(5.0, 2.0, 7.0));
    printf("%d\n",any_int(3.0, 2.0, 2.0));
    printf("%d\n",any_int(3.0, -2.0, 1.0));
    printf("%d\n",any_int(3.6, -2.2, 2.0));
    return 0;
}

B:
/*
Create a function that takes 3 numbers.
Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
Returns false in any other cases.

Examples
any_int(5, 2, 7) ➞ true

any_int(3, 2, 2) ➞ false

any_int(3, -2, 1) ➞ true

any_int(3.6, -2.2, 2) ➞ false



*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool any_int(float a,float b,float c){
    if((a==b+c) || (b==a+c) || (c==a+b)){
        if((a==round(a)) && (b==round(b)) && (c==round(c))){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        return false;
    }
}

int main(){
    printf("%d\n",any_int(5.0, 2.0, 7.0));
    printf("%d\n",any_int(3.0, 2.0, 2.0));
    printf("%d\n",any_int(3.0, -2.0, 1.0));
    printf("%d\n",any_int(3.6, -2.2, 2.0));
    return 0;
}

C:
/*
Create a function that takes 3 numbers.
Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
Returns