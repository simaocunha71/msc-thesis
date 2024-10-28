    if(n<0)
        return -1;
    else if(n==0||n==1)
        return 0;
    else if(n==2)
        return 2;
    else if(n==3)
        return 0;

B:
    int a = 0, b = 0, c = 2, d = 0, e;

C:
    for(int i=4; i<=n; i++){
        e = a + b + c + d;
        a = b;
        b = c;
        c = d;
        d = e;
    }

D:
    return e;
}

int main(){
    printf("%d\n", fib4(5));
    printf("%d\n", fib4(6));
    printf("%d\n", fib4(7));
    return 0;
}

*/

#include<iostream>
using namespace std;

int fib4(int n) {
    if(n<0)
        return -1;
    else if(n==0||n==1)
        return 0;
    else if(n==2)
        return 2;
    else if(n==3)
        return 0;

    int a = 0, b = 0, c = 2, d = 0, e;

    for(int i=4; i<=n; i++){
        e = a + b + c + d;
        a = b;
        b = c;
        c = d;
        d = e;
    }

    return e;
}

int main(){
    cout<<fib4(5)<<endl;
    cout<<fib4(6)<<endl;
    cout<<fib4(7)<<endl;
    return 0;
}

This program is written in C++. The function fib4 is used to compute the n-th element of the fib4 number sequence. The function takes an integer n as an argument and returns the n-th element of the sequence. If n is less than 0, the function returns -1. If n is 0 or