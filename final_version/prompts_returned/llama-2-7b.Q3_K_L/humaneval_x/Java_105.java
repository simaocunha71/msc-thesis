import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8]
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

      If the array is empty, return an empty array:
      arr = []
      return []

      If the array has any strange number ignore it:
      arr = [1, -1 , 55]
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ["One"]
     */
    public List<String> byLength(List<Integer> arr) {
        if (arr.isEmpty()) {
            return new ArrayList<>();
        }

        Collections.sort(arr);
        Collections.reverse(arr);
        int length = arr.size();
        StringBuilder sb = new StringBuilder();
        char[] letters = "OneTwoThreeFourFiveSixSevenEightNine".toCharArray();
        for (int i = 0; i < length - 1; i++) {
            sb.append(letters[arr.get(i) / 10]);
        }
        return Arrays.asList(sb.toString().split(""));
    }
}