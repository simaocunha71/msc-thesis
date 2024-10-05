```java
import java.util.*;
import java.lang.*;

class Solution {
    public String sortNumbers(String numbers) {
        String[] splitNumbers = numbers.split(" ");
        List<Integer> numList = new ArrayList<>();
        for (String s : splitNumbers) {
            switch (s) {
                case "zero":
                    numList.add(0);
                    break;
                case "one":
                    numList.add(1);
                    break;
                case "two":
                    numList.add(2);
                    break;
                case "three":
                    numList.add(3);
                    break;
                case "four":
                    numList.add(4);
                    break;
                case "five":
                    numList.add(5);
                    break;
                case "six":
                    numList.add(6);
                    break;
                case "seven":
                    numList.add(7);
                    break;
                case "eight":
                    numList.add(8);
                    break;
                case "nine":
                    numList.add(9);
                    break;
            }
        }
        Collections.sort(numList);
        List<String> sortedNums = new ArrayList<>();
        for (Integer i : numList) {
            switch (i) {
                case 0:
                    sortedNums.add("zero");
                    break;
                case 1:
                    sortedNums.add("one");
                    break;
                case 2:
                    sortedNums.add("two");
                    break;
                case 3:
                    sortedNums.add("three");
                    break;
                case 4:
                    sortedNums.add("four");
                    break;
                case 5:
                    sortedNums.add("five");
                    break;
                case 6:
                    sortedNums.add("six");
                    break;
                case 7:
                    sortedNums.add("seven");
                    break;
                case 8:
                    sortedNums.add("eight");
                    break;
                case 9:
                    sortedNums.add("nine");
                    break;
            }
        }
        return String.join(" ", sortedNums);
    }
}
```