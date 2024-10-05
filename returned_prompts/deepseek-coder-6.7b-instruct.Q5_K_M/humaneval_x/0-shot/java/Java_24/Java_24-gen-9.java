The function you've written is almost correct, but it has a problem: it will return the first divisor it finds that makes n mod i equal to 0. However, the first divisor of n that's smaller than n is actually the largest one. So, you need to start from n-1 and go down to 1, instead of starting from 1 and going up to n-1.

So, the corrected code is:

```
public int largestDivisor(int n)  {
    for(int i = n-1; i > 0; i--){
        if(n % i == 0){
            return i;
        }
    }
    return -1; 
}
```

This function works by iterating from n-1 down to 1, and checking if n is divisible by the current number (i). If it is, the function returns that number as the largest divisor. If no divisor is found (which would only happen if n is 1), the function returns -1.

Please note that this function does not handle the edge case where n is 1 correctly (since 1 is not a proper divisor of any number), so if you want to handle that edge case, you'll need to add an additional check for that.

Also, if you want to find the largest prime number that divides n, you would need a different function that checks if each number from n-1 down to 2 is a prime divisor of n.

Here is the code for that:

```
public int largestPrimeDivisor(int n)  {
    for(int i = n-1; i > 1; i--){
        if(n % i == 0){
            boolean isPrime = true;
            for(int j = 2; j*j <= i; j++) {
                if(i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if(isPrime) {
                return i;
           