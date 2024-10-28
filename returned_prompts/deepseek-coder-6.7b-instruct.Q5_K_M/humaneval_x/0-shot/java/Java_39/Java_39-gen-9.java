        int a = 0, b = 1, c = 0;
        int count = 0, i = 1;
        while (count < n) {
            c = a + b;
            a = b;
            b = c;
            if (isPrime(c)) {
                count++;
                if (count == n) {
                    return c;
                }
            }
        }
        return -1;
    }

    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main (String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.primeFib(1)); // 2
        System.out.println(sol.primeFib(2)); // 3
        System.out.println(sol.primeFib(3)); // 5
        System.out.println(sol.primeFib(4)); // 13
        System.out.println(sol.primeFib(5)); // 89
    }
}

In this Java program, `primeFib` generates Fibonacci numbers and checks if they are prime using `isPrime` method. If the Fibonacci number is prime, it increments the count. The function returns the nth prime Fibonacci number.
*/

package main

import (
	"fmt"
	"math"
)

func primeFib(n int) int {
	a, b := 0, 1
	c, count, i := 0, 0, 1
	for count < n {
		c = a + b
		a = b
		b = c
		if isPrime(c) {
			count++
			if count == n {
				return c
			}
		}
	}
	return -1
}

func isPrime(n int) bool {
	if n