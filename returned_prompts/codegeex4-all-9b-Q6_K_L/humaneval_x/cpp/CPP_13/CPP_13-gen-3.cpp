/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    if(b==0){
        return a;
    }
    else{
        return greatest_common_divisor(b,a%b);
    }
}

B:
/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    if(a==0){
        return b;
    }
    else{
        return greatest_common_divisor(b,a%b);
    }
}

C:
/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    if(b==0){
        return a;
    }
    else{
        return greatest_common_divisor(a,b%a);
    }
}

D:
/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    if(a==0){
        return b;
    }
    else{
        return greatest_common_divisor(a,b%a);
    }
}

答案：AC
