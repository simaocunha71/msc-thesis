        int count = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++) {
                    int a_i = i * i - i + 1;
                    int a_j = j * j - j + 1;
                    int a_k = k * k - k + 1;

                    if ((a_i + a_j + a_k) % 3 == 0) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
}

I:
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.getMaxTriples(n));

This code seems to work fine but it is not efficient. It has a time complexity of O(n^3) and it's not optimized for large n.

Can you help me optimize this code?

A: I have optimized your code by reducing the time complexity to O(n). Here's the optimized version:

```java
class Solution {
    public int getMaxTriples(int n) {
        int count = 0;
        int[] a = new int[n+1];

        // calculate values of a[i]
        for(int i = 1; i <= n; i++) {
            a[i] = i*i - i + 1;
        }

        // count triplets
        int[] mod = new int[3];
        for(int i = 1; i <= n; i++) {
            count += mod[a[i] % 3];
            mod[a[i] % 3]++;
        }

        return count;
    }
}
```
In this optimized code, we first calculate the values of `a[i]` for `i` from `1` to `n`. Then we count the triplets by keeping track of the remainder of `a[i] % 3` for each `i`.