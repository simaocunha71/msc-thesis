Here's the Java solution:
```java
import java.util.*;

class Solution {
    public String sortNumbers(String numbers) {
        String[] numberals = numbers.split(" ");
        Arrays.sort(numberals, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return getNumber(s1) - getNumber(s2);
            }
        });
        return String.join(" ", numberals);
    }

    private int getNumber(String numberal) {
        switch (numberal) {
            case "zero": return 0;
            case "one": return 1;
            case "two": return 2;
            case "three": return 3;
            case "four": return 4;
            case "five": return 5;
            case "six": return 6;
            case "seven": return 7;
            case "eight": return 8;
            case "nine": return 9;
            default: throw new IllegalArgumentException("Invalid numberal: " + numberal);
        }
    }
}
```
This solution first splits the input string into an array of numberals. Then it sorts the array using a custom comparator that compares the numberals based on their corresponding integer values. Finally it joins the sorted numberals back into a string, separated by spaces. The `getNumber` method is a helper method that converts a numberal string to its corresponding integer value.