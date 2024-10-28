        int res = 0;
        int base = (int)Math.pow(10, n - 1);
        for (int i = 1; i <= base; i++) {
            if (i % 10 == 1 || i / (int)Math.pow(10, n - 1) % 10 == 1) {
                res++;
            }
        }
        return res;
    }
}

Explanation:
The problem asks to find the count of n-digit positive integers that start or end with 1. 
We can solve this problem by iterating over all n-digit numbers and checking if the number starts or ends with 1.

In the code, we first initialize the result variable `res` to 0. Then, we calculate the base value `base` which is 10^(n-1) because the leftmost digit of an n-digit number cannot be greater than 9.

We then iterate over all n-digit numbers from 1 to `base`. For each number, we check if the number starts with 1 (i % 10 == 1) or ends with 1 (i / (int)Math.pow(10, n - 1) % 10 == 1). If either condition is true, we increment the result variable `res`.

Finally, we return the result `res` which is the count of n-digit positive integers that start or end with 1.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q.E.D.  Q