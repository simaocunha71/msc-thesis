    for (int i = n/2; i >= 1; i--){
        if (n % i == 0){
            return i;
        }
    }
}

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Largest divisor: %d", largest_divisor(num));
    return 0;
}
```

This program will find the largest number that divides the number entered evenly, smaller than the entered number.

Please note that the code uses integer division, which means that the result is always an integer.

Also, it starts checking from n/2 and goes down to 1, because any number n can have at least one divisor 1 and the largest number is n itself. So, for any number n, the largest divisor will always be smaller than n/2 + 1.

This code can be further optimized by starting from sqrt(n) and going down to 1, because any number n can have its divisor greater than sqrt(n) paired with a divisor smaller than sqrt(n).

Also, the number 1 is not considered as a divisor of any number, so the loop can start from 2.

Here is the optimized code:

```cpp
#include<bits/stdc++.h>
using namespace std;

int largest_divisor(int n){
    for (int i = sqrt(n); i >= 2; i--){
        if (n % i == 0){
            return n / i;
        }
    }
    return 1;
}

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Largest divisor: %d", largest_divisor(num));
    return 0;
}
```

In this optimized version, we return n / i because i is the divisor of n / i.

This program will find the largest number that divides the number entered evenly, smaller than the entered number.

Please note that the code uses integer division, which means that the result is always an integer.

Also, it starts checking from sqrt(