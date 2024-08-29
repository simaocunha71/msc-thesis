/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
#include<math.h>
using namespace std;
int greatest_common_divisor(int a, int b){
    int gcd;
    if(a==0) return b;
    if(b==0) return a;
    if(a>b) gcd=greatest_common_divisor(a%b,b);
    if(a<b) gcd=greatest_common_divisor(a,b%a);
    return gcd;
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
    if(a%b==0) return b;
    if(b%a==0) return a;
    if(a>b) return greatest_common_divisor(a%b,b);
    if(a<b) return greatest_common_divisor(a,b%a);
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
    if(a==0) return b;
    if(b==0) return a;
    if(a%b==0) return b;
    if(b%a==0) return a;
    if(a>b) return greatest_common_divisor(a%b,b);
    if(a<b) return greatest_common_divisor(a,b%a);
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
    if(a==0) return b;
    if(b==0) return a;
    if(a>b) return greatest_common_divisor(a%b,b);
    if(a<b) return greatest_common_divisor(a,b%a);
    if(a%b==0) return b;
    if(b%a==0) return a;
}

F:
/*
Return a greatest common divisor of two integers