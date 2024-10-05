        String[] numStrings = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] numSort = new String[10];
        String[] nums = numbers.split(" ");
        int count = 0;

        for (String num : nums) {
            for (int i = 0; i < numStrings.length; i++) {
                if (num.equals(numStrings[i])) {
                    numSort[i] = num;
                    count++;
                }
            }
        }

        Arrays.sort(numSort, 0, count);
        String sortedNums = "";

        for (int i = 0; i < count; i++) {
            sortedNums += numSort[i] + " ";
        }
        return sortedNums.trim();
    }

}


A: The algorithm is almost correct, but you should use a map to convert from string to number and vice versa. This way you can sort the numbers in numerical order, not alphabetical order. Here is the corrected code:

```java
import java.util.*;

class Solution {
    public String sortNumbers(String numbers) {
        Map<String, Integer> numMap = new HashMap<String, Integer>() {{
            put("zero", 0);
            put("one", 1);
            put("two", 2);
            put("three", 3);
            put("four", 4);
            put("five", 5);
            put("six", 6);
            put("seven", 7);
            put("eight", 8);
            put("nine", 9);
        }};

        String[] nums = numbers.split(" ");
        Integer[] numSort = new Integer[nums.length];
        int count = 0;

        for (String num : nums) {
            numSort[count++] = numMap.get(num);
        }

        Arrays.sort(numSort, 0, count);
        String sortedNums = "";

        for (int i = 