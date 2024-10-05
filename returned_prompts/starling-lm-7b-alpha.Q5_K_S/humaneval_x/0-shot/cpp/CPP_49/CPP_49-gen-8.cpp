    if(n==0) return 1;
    else if(n%2==0) return modp(n/2,p)*modp(n/2,p)%p;
    else return 1ll*modp(n/2,p)*modp(n/2,p)%p*n%p;
}

/*
Return true if n is a prime number, else return false.
>>> isPrime(3)
true
>>> isPrime(8)
false
>>> isPrime(101)
true
*/
#include<stdio.h>
using namespace std;
bool isPrime(int n){
    if(n==2||n==3) return true;
    if(n%2==0||n<2) return false;
    for(int i=3;i*i<=n;i+=2){
        if(n%i==0) return false;
    }
    return true;
}

/*
Return the nth Fibonacci number.
>>> fib(5)
5
>>> fib(10)
55
>>> fib(20)
6765
*/
#include<stdio.h>
using namespace std;
long long fib(int n){
    if(n==0) return 0;
    if(n==1||n==2) return 1;
    long long f[n+1];
    f[0]=0; f[1]=1; f[2]=1;
    for(int i=3;i<=n;i++) f[i]=f[i-1]+f[i-2];
    return f[n];
}

/*
Return the nth number in the Fibonacci sequence.
>>> fibSeq(5)
[0, 1, 1, 2, 3]
>>> fibSeq(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> fibSeq(20)
[0, 1, 1, 2, 3, 5, 8, 13, 21