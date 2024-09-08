    int i;
    for(i=n-1; i>0; i--){
        if(n%i == 0){
            return i;
        }
    }
    return 0;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The largest divisor is: %d\n", largest_divisor(n));
    return 0;
}

```
Here, `largest_divisor` function iterates from `n-1` to `1` and checks each number to see if it's a divisor of `n`. If it is, it returns that number. If no divisor is found, it returns `0`. In the `main` function, the user is prompted to enter a number, and then the `largest_divisor` function is called with that number as its argument. The result is then printed out.

However, there is a more efficient way to do this. Instead of iterating from `n-1` to `1`, you can iterate from `n/2` down to `1`. This is because a larger factor of `n` must be a multiple of a smaller factor that has already been checked. Here is the updated code:

```c
int largest_divisor(int n){
    int i;
    for(i=n/2; i>0; i--){
        if(n%i == 0){
            return i;
        }
    }
    return 1; // or return 0, depending on your desired behavior
}
```
This version of the function will be faster and more efficient for large values of `n`. It's also worth noting that you can use the `sqrt` function from the `math.h` library to further optimize the function, since a larger factor of `n` must be less than or equal to the square root of `n`. Here is the updated code:

```c
#include <math.h>
int largest_divisor(int n){
    int i;
    for(i=(int)sqrt((double)n); i>0; i--){
        if(n%i == 0){
            return i;
        }
    }
    return 1; // or return 0, depending on your desired behavior
}
```
This version of the function will be even faster and more efficient for large values of `n`. It's also more accurate, since it uses the `sqrt` function to calculate the square root of `n` instead of using a simple division.