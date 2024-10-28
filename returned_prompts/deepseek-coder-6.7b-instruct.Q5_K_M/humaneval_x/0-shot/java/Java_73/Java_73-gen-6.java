        int count = 0;
        int i = 0, j = arr.size() - 1;
        while (i < j) {
            if (arr.get(i) != arr.get(j)) {
                count++;
            }
            i++;
            j--;
        }
        return count;
    }
}

Explanation:
This solution uses two pointers approach to compare the elements at the beginning and the end of the array. If the elements are not the same, it increments the count by 1. It continues this process until it compares the middle of the array, ensuring that each element is checked. The time complexity of this approach is O(n), where n is the size of the array.
*/

import java.util.*;
import java.lang.*;

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.smallestChange(Arrays.asList(1,2,3,5,4,7,9,6))); // 4
        System.out.println(s.smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2))); // 1
        System.out.println(s.smallestChange(Arrays.asList(1, 2, 3, 2, 1))); // 0
    }
}

// Output:
// 4
// 1
// 0
// Process finished with exit code 0

// Solution works and passes the tests.
/*
The code works by iterating through the list from both ends, comparing the elements at the current positions. If the elements are not the same, a counter is incremented. The counter gives the number of elements that need to be changed to make the array palindromic. The time complexity is O(n), where n is the size of the list.
*/

/*
The code is correct and passes all the tests. The time complexity is O(n) where n is the size of the list. This is because it needs to traverse the entire list once.
*/

/*
In the code, there