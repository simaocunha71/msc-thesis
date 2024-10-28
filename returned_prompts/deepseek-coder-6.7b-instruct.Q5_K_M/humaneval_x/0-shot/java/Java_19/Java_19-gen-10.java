        String[] wordNumbers = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] numberWords = numbers.split(" ");
        Arrays.sort(numberWords, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return Arrays.asList(wordNumbers).indexOf(o1) - Arrays.asList(wordNumbers).indexOf(o2);
            }
        });
        return String.join(" ", numberWords);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sortNumbers("three one five"));
    }
}

Explanation:

In this code, we are firstly mapping the numeric strings to their corresponding words. Then, we split the input string into an array of strings using the split() method. We use the Arrays.sort() method to sort the array in ascending order based on the index of the words in the wordNumbers array. Finally, we use the String.join() method to join the elements of the sorted array into a string, separated by a space.

The solution uses Java's built-in sorting function with a custom Comparator. It compares the index of the words in the wordNumbers array to sort the words. The advantage of this solution is that it can handle any number of words and is easy to understand and maintain.

This solution has a time complexity of O(n log n) because of the sorting operation, and a space complexity of O(n) because of the space required for the input string and the sorted array.

The output of the given example "three one five" is "one three five".
*/

// Code:
// import java.util.*;
// import java.lang.*;

// class Solution  {
//     public String sortNumbers(String numbers)  {
//         String[] wordNumbers = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine