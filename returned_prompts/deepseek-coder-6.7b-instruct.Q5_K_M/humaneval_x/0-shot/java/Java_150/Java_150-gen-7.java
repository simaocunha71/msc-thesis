        if (isPrime(n)){
            return x;
        }
        else{
            return y;
        }
    }

    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < Math.sqrt(n) + 1; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

Explanation:
Here, the `xOrY` function takes three integers as input - n, x, and y.

If the value of n is a prime number, it returns the value of x. Otherwise, it returns the value of y.

The `isPrime` function checks if the number is prime or not. If the number is less than or equal to 1, it is not a prime number and the function returns false.

Then, the function loops from 2 to the square root of the number plus 1. If the number is divisible by any of these numbers, it is not a prime number and the function returns false.

If none of these conditions are met, the number is prime and the function returns true.
*/

//Test Cases:
//xOrY(7, 34, 12) should return 34
//xOrY(15, 8, 5) should return 5
//xOrY(2, 10, 20) should return 10
//xOrY(4, 30, 40) should return 40
//xOrY(13, 50, 60) should return 50
//xOrY(17, 70, 80) should return 70
//xOrY(23, 90, 100) should return 90
//xOrY(29, 110, 120) should return 110
//xOrY(31, 130, 140) should return 130
//xOrY(37, 150, 160) should return