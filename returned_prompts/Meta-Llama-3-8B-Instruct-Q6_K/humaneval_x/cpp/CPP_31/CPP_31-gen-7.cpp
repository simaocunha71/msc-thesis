    if(n <= 1)
        return false;
    if(n == 2)
        return true;
    if(n % 2 == 0)
        return false;

    long long limit = sqrt(n);
    for(long long i = 3; i <= limit; i += 2){
        if(n % i == 0)
            return false;
    }
    return true;
}
int main(){
    printf("%d\n",is_prime(6));
    printf("%d\n",is_prime(101));
    printf("%d\n",is_prime(11));
    printf("%d\n",is_prime(13441));
    printf("%d\n",is_prime(61));
    printf("%d\n",is_prime(4));
    printf("%d\n",is_prime(1));
    return 0;
}
B:

```c
#include<stdio.h>
using namespace std;

bool is_prime(long long n) {
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;

    long long limit = sqrt(n);
    for (long long i = 3; i <= limit; i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    printf("%d\n", is_prime(6));  // 0
    printf("%d\n", is_prime(101)); // 1
    printf("%d\n", is_prime(11));  // 1
    printf("%d\n", is_prime(13441)); // 1
    printf("%d\n", is_prime(61));   // 1
    printf("%d\n", is_prime(4));    // 0
    printf("%d\n", is_prime(1));    // 0
    return 0;
}
```

The code provided is a correct implementation of the is_prime function in C++. The function takes a long long integer as input and returns true if the number is prime, and false otherwise.

The function first checks if the number is less than or equal to 1, in which case it is not prime and the function returns false. Then it checks if the number is 2, in which case it is prime and the function returns true.

Next, it checks if the number is even (i.e., divisible by 2), in which case it is