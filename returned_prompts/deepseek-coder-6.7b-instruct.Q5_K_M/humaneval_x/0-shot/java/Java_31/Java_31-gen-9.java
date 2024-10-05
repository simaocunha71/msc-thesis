        if(n <= 1) return false;
        if(n <= 3) return true;

        if(n%2 == 0 || n%3 == 0) return false;

        for(int i = 5; i * i <= n; i += 6) {
            if(n%i == 0 || n%(i + 2) == 0) return false;
        }

        return true;
    }
}


A: Here is the corrected code:

import java.util.*;
import java.lang.*;

class Solution {
    /**
    * Return true if a given number is prime, and false otherwise.
    * @param n number to check
    * @return true if prime, false otherwise
    * @example isPrime(6) // false
    * @example isPrime(101) // true
    * @example isPrime(11) // true
    * @example isPrime(13441) // false
    * @example isPrime(61) // true
    * @example isPrime(4) // false
    * @example isPrime(1) // false
    */
    public boolean isPrime(int n) {
        if(n <= 1) return false;
        if(n <= 3) return true;

        if(n%2 == 0 || n%3 == 0) return false;

        for(int i = 5; i * i <= n; i += 6) {
            if(n%i == 0 || n%(i + 2) == 0) return false;
        }

        return true;
    }
}


A: Your code is correct and it's a good practice to use JavaDoc comments to explain your code. It's a good practice to document your code so other people can understand it.

A: The provided code is correct and it is a good practice to use JavaDoc comments to explain your code. It's also a good practice to document your code so that other people can understand it.

Here is the JavaDoc comment:

/**
* Return true if a given number is prime, and false otherwise.
* @param n number to check
* @return true if prime,