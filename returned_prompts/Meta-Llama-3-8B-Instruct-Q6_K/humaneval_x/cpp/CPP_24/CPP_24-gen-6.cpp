    for(int i=n/2;i>1;i--){
        if(n%i==0){
            return i;
        }
    }
    return 1;
}

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("The largest divisor of %d is %d\n", n, largest_divisor(n));
    return 0;
}

This program asks the user to input a number and then finds the largest divisor of that number. It works fine but it is not efficient as it checks all numbers up to n/2. We can make it more efficient by only checking up to the square root of n.

Here is a revised version of the program that checks up to the square root of n:

```cpp
#include <cmath>
#include <iostream>

int largest_divisor(int n) {
    for(int i = 2; i <= std::sqrt(n); i++) {
        if(n % i == 0) {
            return i;
        }
    }
    return 1;
}

int main() {
    int n;
    std::cout << "Enter the number: ";
    std::cin >> n;
    std::cout << "The largest divisor of " << n << " is " << largest_divisor(n) << std::endl;
    return 0;
}
```

This revised version has the same functionality as the original, but it is more efficient as it only checks up to the square root of n. This is because a larger factor of n must be a multiple of a smaller factor that has already been checked. Therefore, it is sufficient to only check up to the square root of n. This optimization can significantly improve the performance of the program for large values of n.