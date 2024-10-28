        if(array.isEmpty()){
            return array;
        }

        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);

        int first = sortedArray.get(0);
        int last = sortedArray.get(sortedArray.size() - 1);

        if((first + last) % 2 != 0){
            return sortedArray;
        } else {
            Collections.reverse(sortedArray);
            return sortedArray;
        }
    }
}

This solution first checks if the array is empty, if it is it returns the array.
Then it makes a copy of the array and sorts it.
It then gets the first and last values and checks if their sum is odd or even.
If the sum is odd, it returns the sorted array.
If the sum is even, it reverses the sorted array and returns it.
*/

// Your task is to fix the buggy code.
// The code you will fix has a bug in it. The bug is that it doesn't handle the case when the array is empty. 
// The function should return an empty list if the input list is empty.

// Fixed Code:

import java.util.*;
import java.lang.*;

class Solution  {
    public List<Integer> sortArray(List<Integer> array) {

        if(array.isEmpty()){
            return new ArrayList<>();
        }

        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);

        int first = sortedArray.get(0);
        int last = sortedArray.get(sortedArray.size() - 1);

        if((first + last) % 2 != 0){
            return sortedArray;
        } else {
            Collections.reverse(sortedArray);
            return sortedArray;
        }
    }
}

// Test the function with the examples given in the docstring of the function.

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.