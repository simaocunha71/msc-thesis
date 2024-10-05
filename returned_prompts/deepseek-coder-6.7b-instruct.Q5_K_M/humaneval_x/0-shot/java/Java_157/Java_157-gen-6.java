        if (a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)
            return true;
        else
            return false;
    }
}

This solution is correct but not optimized. The time complexity is O(1) and the space complexity is also O(1) which is the best you can have for this problem.


A: Here is the optimized solution:
import java.util.*;

class Solution {
    
    public boolean rightAngleTriangle(int a, int b, int c) {
        // Array to store the sides
        int[] sides = {a, b, c};

        // Sort the sides in ascending order
        Arrays.sort(sides);

        // If square of the largest side is equal to sum of squares of other two sides, it is a right angle triangle
        return sides[2]*sides[2] == sides[0]*sides[0] + sides[1]*senses[1];
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.rightAngleTriangle(3, 4, 5));  // True
        System.out.println(solution.rightAngleTriangle(1, 2, 3));  // False
    }
}

This solution stores the sides in an array and sorts them. Then, it checks if the square of the largest side is equal to the sum of the squares of the other two sides. This is a direct consequence of the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. This approach ensures that the function runs in a constant amount of time and uses a constant amount of space.

A: Here is the optimized solution:

import java.util.*;

class Solution {
    
    public boolean rightAngleTriangle(int a, int b, int c) {
        // Array to store the sides
        int[] sides