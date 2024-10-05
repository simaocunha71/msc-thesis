    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
B:
    for (long long i=5; i*i<=n; i=i+6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}
*/

int main() {
  long long num;
  printf("Enter a number to check if it's prime: ");
  scanf("%lld", &num);
  if(is_prime(num))
    printf("%lld is a prime number.\n", num);
  else
    printf("%lld is not a prime number.\n", num);
  return 0;
}


A: In your code, you need to make a few changes:


*

*You need to include the math library to use the sqrt function. 

*The algorithm should be optimized to check divisibility only up to the square root of n, and by skipping multiples of 2 and 3.

*You need to include the math library to use the sqrt function.


Here's the corrected code:
#include <math.h>

bool is_prime(long long n){
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (long long i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

This code works by first checking if n is less than or equal to 1, in which case it returns false. If n is less than or equal to 3, it returns true. Then it checks if n is divisible by 2 or 3. If it is, the function returns false.

Finally, the loop starts at 5 and increments by 6 each time. Inside the loop, it checks if n