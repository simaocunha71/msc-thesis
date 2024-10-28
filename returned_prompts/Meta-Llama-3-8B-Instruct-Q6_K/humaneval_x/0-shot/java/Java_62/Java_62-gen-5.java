Here is a simple and efficient solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> derivative(List<Integer> xs) {
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i < xs.size(); i++) {
            result.add(i * xs.get(i));
        }
        return result;
    }
}
```

Explanation:

The derivative of a polynomial is calculated by multiplying each coefficient of the polynomial by its corresponding power of x, and then shifting the result to the right. 

In the code above, we iterate over the list of coefficients starting from the second element (since the derivative of the constant term is 0). For each coefficient, we multiply it by its corresponding power of x, which is given by its index in the list (since the first element corresponds to the constant term, the second element corresponds to the term with power 1, and so on). We then add the result to the list of coefficients of the derivative.

The time complexity of this solution is O(n), where n is the number of coefficients in the input list. The space complexity is also O(n), since we need to store the coefficients of the derivative in a new list. 

For example, if the input list is [3, 1, 2, 4, 5], the output list will be [1, 4, 12, 20]. If the input list is [1, 2, 3], the output list will be [2, 6]. 

This solution is simple and efficient, and it works for polynomials of any degree. 

Note: The input list is a list of coefficients of a polynomial, where the first element corresponds to the constant term, the second element corresponds to the term with power 1, and so on. The output list is also a list of coefficients of the derivative of the polynomial, where the first element corresponds to the constant term, the second element corresponds to the term with power 1, and so on. 

This solution assumes that the input list contains at least one element. If the input list is empty, the solution will throw an exception when trying to access the first element. 

If you want to handle the case where the input list is empty, you can add a simple check at the beginning of the method. For example:

```java
public List<Integer> derivative(List<Integer> xs) {
    if (xs.isEmpty()) {
        return new ArrayList<>();
    }
    //