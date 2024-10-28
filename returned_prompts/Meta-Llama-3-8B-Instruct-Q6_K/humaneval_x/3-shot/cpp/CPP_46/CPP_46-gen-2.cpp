    if (n<0 || n>3)
    return -1;
    int f0=0, f1=0, f2=2, f3=0;
    for (int i=4; i<=n; i++)
    {
        int f4=f0+f1+f2+f3;
        f0=f1;
        f1=f2;
        f2=f3;
        f3=f4;
    }
    return f3;
}
//or
#include<vector>
using namespace std;
int fib4(int n){
    if (n<0 || n>3)
        return -1;
    vector<int> fib4_sequence={0,0,2,0};
    for (int i=4; i<=n; i++)
        fib4_sequence.push_back(fib4_sequence[i-1]+fib4_sequence[i-2]+fib4_sequence[i-3]+fib4_sequence[i-4]);
    return fib4_sequence[n];
}
//or
#include<vector>
#include<array>
using namespace std;
int fib4(int n){
    if (n<0 || n>3)
        return -1;
    array<int,4> fib4_sequence={0,0,2,0};
    for (int i=4; i<=n; i++)
    {
        int f4=fib4_sequence[0]+fib4_sequence[1]+fib4_sequence[2]+fib4_sequence[3];
        fib4_sequence[0]=fib4_sequence[1];
        fib4_sequence[1]=fib4_sequence[2];
        fib4_sequence[2]=fib4_sequence[3];
        fib4_sequence[3]=f4;
    }
    return fib4_sequence[3];
}
//or
#include<array>
using namespace std;
int fib4(int n){
    if (n<0 || n>3)
        return -1;
    array<int,4> fib4_sequence={0,0,2,0};
    for (int i=4; i<=n; i++)
        fib4_sequence[i%4]=fib4_sequence[(i-1)%4]+fib4_sequence[(i-2)%4]+fib4_sequence[(i-3)%4]+fib4_sequence[(i-4)%4];
    return fib4_sequence[n%4];
}
//or
#include<vector>
using namespace std;
int fib4(int n){
    if (n<0 || n>3