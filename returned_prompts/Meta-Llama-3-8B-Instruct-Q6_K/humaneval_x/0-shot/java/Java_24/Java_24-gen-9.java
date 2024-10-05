        int i = n;
        while(i > 1) {
            if(n % i == 0) {
                return i;
            }
            i--;
        }
        return 1;
    }

Explanation:
The function `largestDivisor` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`.

The function starts by initializing a variable `i` to the value of `n`. It then enters a while loop that continues until `i` is greater than 1.

 Inside the loop, the function checks if `n` is divisible by `i` (i.e., if `n % i` is equal to 0). If it is, the function returns `i` as the largest divisor.

If `n` is not divisible by `i`, the function decrements `i` by 1 and repeats the loop.

If the loop completes without finding a divisor, the function returns 1, indicating that the largest divisor is 1 (i.e., `n` itself).

For example, if `n` is 15, the function will return 5, which is the largest number that divides 15 evenly, smaller than 15. If `n` is 1, the function will return 1, as there is no number smaller than 1 that divides 1 evenly.