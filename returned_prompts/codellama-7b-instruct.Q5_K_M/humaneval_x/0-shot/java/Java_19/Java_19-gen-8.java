import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sortNumbers("three one five")
    "one three five"
     */
    public String sortNumbers(String numbers) {
        List<Integer> nums = new ArrayList<>();
        for (String number : numbers.split(" ")) {
            if (number.equals("zero")) {
                nums.add(0);
            } else if (number.equals("one")) {
                nums.add(1);
            } else if (number.equals("two")) {
                nums.add(2);
            } else if (number.equals("three")) {
                nums.add(3);
            } else if (number.equals("four")) {
                nums.add(4);
            } else if (number.equals("five")) {
                nums.add(5);
            } else if (number.equals("six")) {
                nums.add(6);
            } else if (number.equals("seven")) {
                nums.add(7);
            } else if (number.equals("eight")) {
                nums.add(8);
            } else {
                nums.add(9);
            }
        }
        Collections.sort(nums);
        return String.join(" ", nums.toString());
    }
}