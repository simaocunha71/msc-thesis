        if (n == 0)
            return 1;

        int res = 1;
        while (n > 0) {
            if ((n & 1) == 1)
                res = (res * 2) % p;
            n = n >> 1;
            if (n > 0)
                res = (res * res) % p;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.modp(3, 5));
        System.out.println(s.modp(1101, 101));
        System.out.println(s.modp(0, 101));
        System.out.println(s.modp(3, 11));
        System.out.println(s.modp(100, 101));
    }
}

In the modp function, we use the property of exponentiation that says a^(m*n) = (a^m)^n and a^(m/2) = sqrt(a^m). We apply this property in the while loop and we also take care of p to prevent overflow.
This solution uses bitwise operations for optimizing the function. If n is even, it means that the last bit of n is 0, so we can ignore this bit and move to the next bit. If n is odd, we multiply the result by 2 and then move to the next bit.
In each step, we also square the result and take it modulo p, so we don't overflow the int.
This solution has a time complexity of O(log n), which is the best you can achieve for this problem.
    */
}

//src/main/java/com/javacode/algorithms/modular/exponentiation/Main.java
package com.javacode.algorithms.modular.exponentiation;

import com.javacode.algorithms.modular.exponentiation.Solution;

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out