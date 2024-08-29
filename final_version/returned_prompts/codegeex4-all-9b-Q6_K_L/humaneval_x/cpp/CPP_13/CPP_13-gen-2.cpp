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
    int i;
    for(i=2;i<=a;i++){
        if(a%i==0 && b%i==0){
            return i;
        }
    }
    return 1;
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
    int i;
    for(i=2;i<=b;i++){
        if(a%i==0 && b%i==0){
            return i;
        }
    }
    return 1;
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
    int i;
    for(i=2;i<=a || b;i++){
        if(a%i==0 && b%i==0){
            return i;
        }
    }
    return 1;
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
    int i;
    for(i=2;i<=a && b;i++){
        if(a%i==0 && b%i==0){
            return i;
        }
    }
    return 1;
}

E:
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
    int i;
    for(i=2;i<=a && b<=a;i++){
        if(a%i==0 && b%i==0){
            return i;
        }
    }
    return 1;
}
