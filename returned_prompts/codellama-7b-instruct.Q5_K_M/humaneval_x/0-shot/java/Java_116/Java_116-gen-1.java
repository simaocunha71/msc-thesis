import java.util.*;
import java.lang.*;

class Solution {
    /**
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.
    <p>
    It must be implemented like this:
    >>> sortArray(Arrays.asList(1, 5, 2, 3, 4)).equals(Arrays.asList(1, 2, 3, 4, 5))
    >>> sortArray(Arrays.asList(-2, -3, -4, -5, -6)).equals(Arrays.asList(-6, -5, -4, -3, -2))
    >>> sortArray(Arrays.asList(1, 0, 2, 3, 4)).equals(Arrays.asList(0, 1, 2, 3, 4))
     */
    public List<Integer> sortArray(List<Integer> arr) {
        List<Integer> sorted = new ArrayList<Integer>();
        for (int i = 0; i < arr.size(); i++) {
            int count = 0;
            String binary = Integer.toBinaryString(arr.get(i));
            for (int j = 0; j < binary.length(); j++) {
                if (binary.charAt(j) == '1') {
                    count++;
                }
            }
            sorted.add(arr.get(i));
        }
        Collections.sort(sorted, new Comparator<Integer>() {
            public int compare(Integer o1, Integer o2) {
                int count1 = 0;
                String binary1 = Integer.toBinaryString(o1);
                for (int j = 0; j < binary1.length(); j++) {
                    if (binary1.charAt(j) == '1') {
                        count1++;
                    }
                }
                int count2 = 0;
                String binary2 = Integer.toBinaryString(o2);
                for (int j = 0; j < binary2.length(); j++)