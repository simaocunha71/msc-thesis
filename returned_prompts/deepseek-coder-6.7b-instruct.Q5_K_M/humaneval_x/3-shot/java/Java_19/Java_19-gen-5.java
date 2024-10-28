        Map<String, Integer> stringToNumber = new HashMap<>();
        stringToNumber.put("zero", 0);
        stringToNumber.put("one", 1);
        stringToNumber.put("two", 2);
        stringToNumber.put("three", 3);
        stringToNumber.put("four", 4);
        stringToNumber.put("five", 5);
        stringToNumber.put("six", 6);
        stringToNumber.put("seven", 7);
        stringToNumber.put("eight", 8);
        stringToNumber.put("nine", 9);

        Map<Integer, String> numberToString = new HashMap<>();
        numberToString.put(0, "zero");
        numberToString.put(1, "one");
        numberToString.put(2, "two");
        numberToString.put(3, "three");
        numberToString.put(4, "four");
        numberToString.put(5, "five");
        numberToString.put(6, "six");
        numberToString.put(7, "seven");
        numberToString.put(8, "eight");
        numberToString.put(9, "nine");

        List<Integer> numberList = new ArrayList<>();
        for (String s : numbers.split(" ")) {
            numberList.add(stringToNumber.get(s));
        }

        Collections.sort(numberList);

        StringBuilder result = new StringBuilder();
        for (Integer i : numberList) {
            result.append(numberToString.get(i)).append(" ");
        }

        return result.toString().trim();
    }
}


A: import java.util.*;
import java.lang.*;

class Solution 
{
    /**
    Given a string of characters, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
    >>> firstUniqChar("leetcode")
    0
      */
    public int firstUniqChar(String s) 
    {
        int[] freq = new int[256];
       