        // Check if the sum of the lengths of any two sides is greater than the
        // third side.
        if ((a + b > c) && (a + c > b) && (b + c > a)) {
            // Calculate the square of the sides.
            int a_square = a * a;
            int b_square = b * b;
            int c_square = c * c;

            // Check if the square of the sum of any two sides is equal to
            // the square of the third side.
            if ((a_square + b_square == c_square) || (a_square + c_square == b_square) || (b_square + c_square == a_square)) {
                return true;
            }
        }

        return false;
    }

}  // class Solution

Explanation:
The given problem is to find whether a triangle is right-angled or not, given the
lengths of the three sides of the triangle.

The solution first checks if the sum of the lengths of any two sides is greater
than the third side, which is a necessary condition for a triangle to be formed.

If the necessary condition is satisfied, the solution then calculates the square
of the sides and checks if the square of the sum of any two sides is equal to
the square of the third side. This is a sufficient condition for a triangle to be
right-angled.

If both conditions are satisfied, the function returns true, indicating that the
triangle is right-angled. Otherwise, it returns false.  // End of Solution

Time Complexity: O(1)
Space Complexity: O(1)  // End of Explanation

Note:
This problem can be solved using the Pythagorean theorem, which states that in a
right-angled triangle, the square of the hypotenuse side is equal to the sum of
the squares of the other two sides. This theorem can be used to check if a
triangle is right-angled or not, given the lengths of the three sides.

However, in this solution, we have used the necessary and sufficient conditions
for a triangle to be right-angled, which are more general and do not require the
Pythagorean theorem.  // End of Note

This solution works for all inputs, including invalid inputs. For example, if the
input lengths do not form a valid triangle (e.g., one side is longer than the sum
of the other two sides), the function will still return false.  // End of