        // Sorting the given lengths in ascending order
        int[] sides = {a, b, c};
        Arrays.sort(sides);

        // Formula to check if triangle is right angled: 
        // square of the hypotenuse should be equal to the sum of squares of other two sides
        return Math.pow(sides[2], 2) == Math.pow(sides[0], 2) + Math.pow(sides[1], 2);
    }
}

This solution first sorts the lengths of the sides in ascending order. After that, it checks if the square of the largest side (hypotenuse) is equal to the sum of squares of the other two sides. If it is, then the triangle is right angled, otherwise it's not.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.rightAngleTriangle(3, 4, 5));  // Expected output: true
        System.out.println(solution.rightAngleTriangle(1, 2, 3));  // Expected output: false
    }
}

/*
Output:
true
false
*/

// This code will work if you run it on your local machine.
// If you want to test it, just copy and paste the code into your IDE.
// And make sure you have imported the necessary libraries.
// Happy coding :)
```

## **Explanation**

This problem is about understanding the properties of right-angled triangle. 

In a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. 

We can use this property to check if a triangle is right-angled. 

First, we sort the lengths of the sides of the triangle in ascending order. After sorting, the largest side is at the last index (`sides[2]`), and the other two sides are at the first two indices (`sides[0]`