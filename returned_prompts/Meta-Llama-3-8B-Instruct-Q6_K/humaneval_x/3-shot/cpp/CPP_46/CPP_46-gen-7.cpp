    if (n<0 || n>3)
        return -1;
    int a=0,b=0,c=2,d=0;
    for (int i=3;i<=n;i++)
    {
        int temp=a+b+c;
        a=b;
        b=c;
        c=temp;
        d=temp;
    }
    return d;
}
// or
#include<stdio.h>
#include<vector>
using namespace std;
int fib4(int n){
    vector<int> fib4_seq(4);
    fib4_seq[0] = 0;
    fib4_seq[1] = 0;
    fib4_seq[2] = 2;
    fib4_seq[3] = 0;
    for(int i=4; i<=n; i++){
        fib4_seq[i%4] = fib4_seq[(i-1)%4] + fib4_seq[(i-2)%4] + fib4_seq[(i-3)%4];
    }
    return fib4_seq[n%4];
}
// or
#include<stdio.h>
#include<vector>
using namespace std;
int fib4(int n){
    vector<int> fib4_seq(n+1);
    fib4_seq[0] = 0;
    fib4_seq[1] = 0;
    fib4_seq[2] = 2;
    fib4_seq[3] = 0;
    for(int i=4; i<=n; i++){
        fib4_seq[i] = fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4];
    }
    return fib4_seq[n];
}
// or
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
int fib4(int n){
    if (n<0 || n>3)
        return -1;
    double phi = (1 + sqrt(5)) / 2;
    double psi = (1 - sqrt(5)) / 2;
    double fib4_seq = 0;
    for(int i=0; i<n; i++){
        fib4_seq = pow(phi, i) - pow(psi, i);
        fib4_seq = round(fib4_seq);
    }
    return fib4_seq;
} // Note that the last solution is not exact, it's an approximation. The other solutions are exact.