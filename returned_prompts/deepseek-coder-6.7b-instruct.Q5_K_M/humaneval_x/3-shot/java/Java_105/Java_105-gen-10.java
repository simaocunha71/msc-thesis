        List<String> res = new ArrayList<>();
        Map<Integer, String> numMap = new HashMap<Integer, String>() {{
            put(1, "One"); put(2, "Two"); put(3, "Three");
            put(4, "Four"); put(5, "Five"); put(6, "Six");
            put(7, "Seven"); put(8, "Eight"); put(9, "Nine");
        }};

        List<Integer> validNums = new ArrayList<>();
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                validNums.add(num);
            }
        }

        Collections.sort(validNums, Collections.reverseOrder());
        for (int num : validNums) {
            res.add(numMap.get(num));
        }

        return res;
    }
}


A: Here is the correct answer. The error was the missing of the brackets in the code.

A: 
Your code is almost correct, but I noticed that you forgot to close the brackets. Here is the corrected code:

import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
      */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for(int i = 0; i < numbers.size() - 1; i++) {
            for(int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if(distance < threshold) {
                    return true;
                }
