The problem is asking to sort the numbers in a given string from smallest to largest. The given string contains numbers from 'zero' to 'nine' and valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.

Here is a Java solution using a HashMap to map the string values to their corresponding integer values, then sorting the string based on the integer values:

```java
import java.util.*;

class Solution {
    public String sortNumbers(String numbers) {
        String[] numArray = numbers.split(" ");
        Map<String, Integer> map = new HashMap<>();
        map.put("zero", 0);
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        map.put("four", 4);
        map.put("five", 5);
        map.put("six", 6);
        map.put("seven", 7);
        map.put("eight", 8);
        map.put("nine", 9);

        List<String> sortedList = new ArrayList<>();
        for (String num : numArray) {
            sortedList.add(num);
        }
        sortedList.sort((a, b) -> map.get(a).compareTo(map.get(b)));

        return String.join(" ", sortedList);
    }
}
```

This solution first splits the input string into an array of strings, then creates a HashMap to map the string values to their corresponding integer values. It then creates a list to store the string values, sorts the list based on the integer values using the HashMap, and finally joins the sorted list into a string with spaces in between. The sorted string is then returned.