        int sum = 0;
        for (int i = 0; i < k; i++) {
            if (arr.get(i) <= 99) {
                sum += arr.get(i);
            }
        }
        return sum;
    }
}

This solution works by iterating through the first k elements of the array, checking if each element is 2 digits or less and if it is, adding it to the sum.

The time complexity of this solution is O(k), as it iterates through the first k elements of the array once. The space complexity is O(1), as it only uses a constant amount of space to store the sum and the iteration variables.
*/

// Example usage:

import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> arr = Arrays.asList(111,21,3,4000,5,6,7,8,9);
        int k = 4;
        int result = solution.addElements(arr, k);
        System.out.println(result);  // Output: 24
    }
}

/*
This code creates a Solution object and calls the addElements method on it, passing in the arr list and the integer k. It then prints the result of the method call.
*/

// Solution:

/*
The solution is correct as it correctly calculates the sum of the elements with at most two digits from the first k elements of the array. The function iterates through the first k elements of the array and checks if each element is less than or equal to 99 (two digits). If it is, it adds the element to the sum. The sum is then returned.
*/

// Complexity:

/*
The time complexity of the solution is O(k), as it iterates through the first k elements of the array once. The space complexity is O(1), as it only uses a constant amount of space to store the sum and the iteration variables.
*/

// Test Case:

/*
The provided test case works correctly. The function correctly adds the elements 21 and 3, which