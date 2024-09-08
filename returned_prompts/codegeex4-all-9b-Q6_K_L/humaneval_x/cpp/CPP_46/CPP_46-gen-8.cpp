/*
fib4(0) -> 0
fib4(1) -> 0
fib4(2) -> 2
fib4(3) -> 0
fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
*/
#include <iostream>
using namespace std;
int fib4(int n){
    int fib[4] = {0, 0, 2, 0};
    if(n < 4){
        return fib[n];
    }
    for(int i = 4; i <= n; i++){
        int temp = fib[0] + fib[1] + fib[2] + fib[3];
        fib[0] = fib[1];
        fib[1] = fib[2];
        fib[2] = fib[3];
        fib[3] = temp;
    }
    return fib[3];
}
int main()
{
    cout<<fib4(5)<<endl;
    return 0;
}
*/