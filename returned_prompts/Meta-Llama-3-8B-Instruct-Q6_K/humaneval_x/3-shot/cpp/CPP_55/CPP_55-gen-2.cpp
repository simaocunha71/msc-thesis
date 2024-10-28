    if (n==1) return 1;
    if (n==2) return 1;
    int fib_n_1 = 1;
    int fib_n_2 = 1;
    int result;
    for (int i=3;i<=n;i++)
    {
        result=fib_n_1+fib_n_2;
        fib_n_2=fib_n_1;
        fib_n_1=result;
    }
    return result;
} //or use memoization
#include <unordered_map>
unordered_map<int, int> memo;
int fib(int n){
    if (n==1) return 1;
    if (n==2) return 1;
    if (memo.count(n)) return memo[n];
    int result=fib(n-1)+fib(n-2);
    memo[n]=result;
    return result;
} //or use dynamic programming
int fib(int n){
    if (n==1) return 1;
    if (n==2) return 1;
    int fib[n+1];
    fib[1]=1;
    fib[2]=1;
    for (int i=3;i<=n;i++)
    {
        fib[i]=fib[i-1]+fib[i-2];
    }
    return fib[n];
}  //or use closed form
int fib(int n){
    if (n==1) return 1;
    if (n==2) return 1;
    double sqrt_5 = sqrt(5);
    double phi = (1 + sqrt_5) / 2;
    double psi = (1 - sqrt_5) / 2;
    return round(pow(phi, n) - pow(psi, n));
} 
