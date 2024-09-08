    int fib[50],i,j;
    fib[0]=0;
    fib[1]=1;
    for(i=2;i<=n;i++){
        fib[i]=fib[i-1]+fib[i-2];
    }
    for(i=0;i<n;i++){
        if(fib[i]>1){
            for(j=2;j<=fib[i]/2;j++){
                if(fib[i]%j==0){
                    break;
                }
            }
            if(j==fib[i]/2+1){
                return fib[i];
            }
        }
    }
}
int main()
{
    printf("%d\n",prime_fib(5));
    return 0;
}
B:
```
def prime_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    if is_prime(b):
        return b

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```
C:
```
#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int prime_fib(int n) {
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        int temp = a;
        a = b;
        b = temp + b;
    }
    if (is_prime(b)) return b;
    return -1;  // not a prime fibonacci number
}

int main() {
    printf("%d\n", prime_fib(5));
    return 0;
}
```
D:
```
#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int prime_fib(int n) {
    int a = 0, b = 1;
    for (int i = 