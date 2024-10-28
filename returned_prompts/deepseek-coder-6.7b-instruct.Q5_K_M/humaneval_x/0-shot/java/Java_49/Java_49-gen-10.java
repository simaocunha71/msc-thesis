        if(n == 0){
            return 1;
        }

        int temp = 1;
        for(int i = 0; i < n; i++){
            temp *= 2;
            temp %= p;
        }

        return temp;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.modp(3, 5)); // 3
        System.out.println(sol.modp(1101, 101)); // 2
        System.out.println(sol.modp(0, 101)); // 1
        System.out.println(sol.modp(3, 11)); // 8
        System.out.println(sol.modp(100, 101)); // 1
    }
}
```

**Explanation:**

The problem is asking for a function that returns the value of 2^n modulo p. This essentially means that we are calculating the remainder of the division of 2^n by p. The modulo operation is a mathematical operation that returns the remainder of a division.

In this solution, we are calculating 2^n (which is a very large number) in a loop and at each step taking modulo p to keep the number manageable. This way we avoid overflow errors that can occur with large numbers.

The function modp takes two parameters, n and p, where n is the power to which 2 is raised and p is the modulus. It returns the remainder of the division of 2^n by p.

In the main function, we are calling this function with different values of n and p to test its correctness.

The complexity of this solution is O(n) as we are performing a single loop from 0 to n.

**Constraints:**

1 <= n <= 10^4

1 <= p <= 10^9

**Note:**

Due to the large size of the numbers, this code might not run correctly in some online compilers. Please use a local or an online Java compiler to run the code.

The main function is for testing the modp function.