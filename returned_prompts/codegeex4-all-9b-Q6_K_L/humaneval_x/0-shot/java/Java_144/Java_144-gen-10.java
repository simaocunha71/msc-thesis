Here is the Java code that implements the requested function:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        int numeratorX = Integer.parseInt(x.split("/")[0]);
        int denominatorX = Integer.parseInt(x.split("/")[1]);
        int numeratorN = Integer.parseInt(n.split("/")[0]);
        int denominatorN = Integer.parseInt(n.split("/")[1]);

        int numeratorResult = numeratorX * numeratorN;
        int denominatorResult = denominatorX * denominatorN;

        return numeratorResult % denominatorResult == 0;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.simplify("1/5", "5/1")); // true
        System.out.println(solution.simplify("1/6", "2/1")); // false
        System.out.println(solution.simplify("7/10", "10/2")); // false
    }
}
```

In this code, the `simplify` method first splits the input strings `x` and `n` by "/" to get the numerator and denominator of each fraction. Then, it calculates the numerator and denominator of the result by multiplying the numerators and denominators of `x` and `n`. Finally, it checks if the numerator of the result is divisible by the denominator (i.e., the result is a whole number) by using the modulo operator. If the result is a whole number, the method returns `true`; otherwise, it returns `false`.