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
    if(b == 0){
        return a;
    }
    else{
        return greatest_common_divisor(b, a % b);
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
    if(a == 0){
        return b;
    }
    else{
        return greatest_common_divisor(b % a, a);
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
    if(a == 0){
        return b;
    }
    else if(b == 0){
        return a;
    }
    else{
        return greatest_common_divisor(b, a % b);
    }
}

正确答案是 D。

A 是错误的，因为它没有处理当 a 为 0 的情况。

B 是错误的，因为它没有处理当 b 为 0 的情况。

C 是错误的，因为它在计算余数时使用了错误的参数顺序。

D 是正确的，它处理了当 a 或 b 为 0 的情况，并且正确地计算了余数。
