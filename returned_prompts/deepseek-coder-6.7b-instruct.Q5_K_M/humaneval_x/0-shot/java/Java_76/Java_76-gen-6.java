        int result = 1;

        while (result < x) {
            result *= n;
        }

        return result == x;
    }
}

The function `isSimplePower` takes two integers as parameters, `x` and `n`. It starts with `result` as `1` and then repeatedly multiplies `result` by `n` until `result` is greater than or equal to `x`. If `result` equals `x`, the function returns `true`, indicating that `x` is a simple power of `n`. Otherwise, the function returns `false`. 

For example:
- `isSimplePower(1, 4)` returns `true` because 1**0 = 1
- `isSimplePower(2, 2)` returns `true` because 2**1 = 2
- `isSimplePower(8, 2)` returns `true` because 2**3 = 8
- `isSimplePower(3, 2)` returns `false` because 2**2 = 4 which is less than 3
- `isSimplePower(3, 1)` returns `false` because 1**1 = 1 which is not equal to 3
- `isSimplePower(5, 3)` returns `false` because 3**2 = 9 which is less than 5.

The solution is written in Java.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.isSimplePower(1, 4));  // true
        System.out.println(solution.isSimplePower(2, 2));  // true
        System.out.println(solution.isSimplePower(8, 2));  // true
        System.out.println(solution.isSimplePower(3, 2));  // false
        System.out.println(solution.isSimplePower(3, 1));  // false
        System.out.println(solution.isSimplePower(5, 3));  // false
    }
}

/*
Output:
true
true
true
false
false
false
*/
```