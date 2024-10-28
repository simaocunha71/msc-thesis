Here is a Python solution for the problem:

```Python
def uniqueDigits(x):
    return sorted([num for num in x if not any(int(digit) % 2 == 0 for digit in str(num))])
```

Here is a Java solution for the problem:

```Java
import java.util.*;

public class Main {
    public static List<Integer> uniqueDigits(int[] x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (!hasEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    public static boolean hasEvenDigit(int num) {
        String str = String.valueOf(num);
        for (char c : str.toCharArray()) {
            if (Integer.parseInt(String.valueOf(c)) % 2 == 0) {
                return true;
            }
        }
        return false;
    }
}
```

The idea behind both solutions is to iterate over the list of numbers and check if any of the digits in the number is even. If not, then the number doesn't have any even digit and is added to the result list. The result list is then sorted before being returned.

In the Python solution, this is done using a list comprehension and the `any` function to check if any digit in the number is even. In the Java solution, this is done by converting the number to a string and then iterating over the characters in the string to check if any of them are even. The `hasEvenDigit` method is used to check if a number has any even digit. The `uniqueDigits` method is used to find all numbers in the list that don't have any even digit and return them in a sorted list.