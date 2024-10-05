    /*
    compute the power of 2 modulo p
    */
    int result = 1;
    while(n > 0){
        if(n & 1)
            result = (result * 2) % p;
        n = n >> 1;
        result %= p;
    }
    return result;
}

int main(){
    printf("%d\n",modp(3,5));
    printf("%d\n",modp(1101,101));
    printf("%d\n",modp(0,101));
    printf("%d\n",modp(3,11));
    printf("%d\n",modp(100,101));
    return 0;
}


A: The code you posted is in C++, but I interpreted your question to be in C, as you were using printf. So, here is the C version:

```C
#include <stdio.h>

int modp(int n, int p) {
    int result = 1;
    while(n > 0) {
        if(n & 1)
            result = (result * 2) % p;
        n = n >> 1;
        result %= p;
    }
    return result;
}

int main() {
    printf("%d\n", modp(3, 5));
    printf("%d\n", modp(1101, 101));
    printf("%d\n", modp(0, 101));
    printf("%d\n", modp(3, 11));
    printf("%d\n", modp(100, 101));
    return 0;
}
```

This code will print the result of modp(3,5), modp(1101,101), modp(0,101), modp(3,11), and modp(100,101).

Please note that this code is using bitwise operations to compute the power of 2 modulo p. It's a common technique used in competitive programming to optimize code execution time.
