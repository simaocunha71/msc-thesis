        if (n == 1) {
            return 1;
        }
        for (int i = n / 2; i > 1; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }
}

Solution:
The function largestDivisor() takes an integer n as input and returns the largest number that divides n evenly, smaller than n. 

In the case where n is equal to 1, the function returns 1, since the only divisor of 1 is 1 itself.

For other values of n, the function iterates from n/2 down to 2, checking each number to see if it is a divisor of n. The first number it finds that is a divisor is the largest divisor, so it returns that number. 

If no divisors are found, the function returns 1, since the smallest divisor of any number is 1. 

The time complexity of this function is O(n), since it iterates from n/2 down to 2. The space complexity is O(1), since it only uses a constant amount of space to store the variables. 

For example, if the input is 15, the function will return 5, since 5 is the largest number that divides 15 evenly and is smaller than 15.  