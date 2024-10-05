        // sort the sides in ascending order
        int[] sides = {a, b, c};
        Arrays.sort(sides);

        // check if the square of the largest side is equal to the sum of the squares of the other two sides
        return Math.pow(sides[2], 2) == Math.pow(sides[0], 2) + Math.pow(sides[1], 2);
    }
}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.rightAngleTriangle(3, 4, 5)); // prints true
        System.out.println(s.rightAngleTriangle(1, 2, 3)); // prints false
    }
}

This program sorts the lengths of the three sides of a triangle in ascending order, then checks if the square of the longest side (the hypotenuse) is equal to the sum of the squares of the other two sides (the sides opposite the right angle). If so, it returns true, meaning the triangle is a right-angled triangle. Otherwise, it returns false.

The time complexity of this solution is O(1) because it performs a constant number of operations regardless of the size of the input. The space complexity is also O(1) because it uses a constant amount of space to store the input and the sorted sides.

Please note that this solution assumes that the inputs are always valid (i.e., they represent the lengths of a triangle). If you want to handle invalid inputs, you should add appropriate error checking.
