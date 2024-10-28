        int[] sides = {a, b, c};
        Arrays.sort(sides);
        return Math.pow(sides[0], 2) + Math.pow(sides[1], 2) == Math.pow(sides[2], 2);
    }
}

Here I used the Pythagorean theorem to solve the problem. Firstly, I sorted the sides in ascending order to ensure that the longest side is in the position c. Then I used the theorem to check if the triangle is right-angled.

Also, the method returns true if the triangle is right-angled and false otherwise.

This solution has a time complexity of O(1) as it does not depend on the size of the input, and a space complexity of O(1) because it uses a constant amount of space.

This solution is correct and efficient.

However, the problem statement mentioned that the angles of the triangle are right-angled, not the sides. If the angles are required to be checked, the problem would need to provide additional information.

In the case of the problem statement, the solution works perfectly.
*/
