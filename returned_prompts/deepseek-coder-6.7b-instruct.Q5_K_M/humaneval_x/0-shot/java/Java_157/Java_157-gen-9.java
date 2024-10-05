        // sort the sides of the triangle
        int[] sides = {a, b, c};
        Arrays.sort(sides);

        // check if one angle is 90 degrees
        return Math.pow(sides[0], 2) + Math.pow(sides[1], 2) == Math.pow(sides[2], 2);
    }
}

Explanation:
The function sorts the sides of the triangle in ascending order. This way, the sides of the triangle will be sorted such that a^2 + b^2 = c^2 holds if and only if the triangle is a right-angled triangle.
*/

class Main{
    public static void main(String[] args){
        Solution sol = new Solution();
        System.out.println(sol.rightAngleTriangle(3, 4, 5)); // should return true
        System.out.println(sol.rightAngleTriangle(1, 2, 3)); // should return false
    }
}

/*
Output:
true
false
*/

// Time Complexity: O(1)
// Space Complexity: O(1)
// since we are storing only the inputs in the array and sorting the array takes O(nlogn) time.
// Here, n is constant as we are always sorting 3 elements. Hence, time complexity remains O(1).
// Space Complexity is also O(1) as we are using a constant amount of space to store the inputs and the sorted array.

// The solution is efficient as it makes use of mathematical properties of right-angled triangles and does not involve any loops or recursive calls.
// It has a time complexity of O(1) as it performs a constant number of operations regardless of the input size.
// The space complexity is also O(1) as it uses a constant amount of space to store the input values and the sorted array.

// Overall, the solution is very efficient and meets the requirements of the problem.

// This solution assumes that the input values are always valid and that the triangle is not a degenerate triangle (i.e., the sum of the lengths of any two sides is less than the length of the third side).

// If the input values