Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        List<Integer> sortedArr = new ArrayList<>();

        // Filter out integers that are not between 1 and 9 inclusive
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sortedArr.add(num);
            }
        }

        // Sort the filtered array
        Collections.sort(sortedArr);

        // Reverse the sorted array
        Collections.reverse(sortedArr);

        // Replace each digit by its corresponding name
        for (int num : sortedArr) {
            result.add(getDigitName(num));
        }

        return result;
    }

    private String getDigitName(int num) {
        switch (num) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
            case 4:
                return "Four";
            case 5:
                return "Five";
            case 6:
                return "Six";
            case 7:
                return "Seven";
            case 8:
                return "Eight";
            case 9:
                return "Nine";
            default:
                return "";
        }
    }
}
```



Here's the explanation of the code:

1. First, we create an empty list `result` to store the final output and an empty list `sortedArr` to store the filtered and sorted integers.
2. We iterate through the input array `arr` and filter out integers that are not between 1 and 9 inclusive. We add the filtered integers to `sortedArr`.
3. We sort `sortedArr` in ascending order using the `Collections.sort()` method.
4. We reverse `sortedArr` using the `Collections.reverse()` method.
5. We iterate through `sortedArr` and replace each digit by its corresponding name using the `getDigitName()` method. We add each digit name to `result`.
6. Finally, we return `result`.

The `getDigitName()` method is a helper method that takes an integer as input and returns the corresponding digit name. It uses a switch statement to map each digit to its corresponding name. If the input integer is not between 1 and 9 inclusive, the method returns an empty string.