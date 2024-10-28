        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1;
        }
        double s = (a + b + c) / 2;
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        return Math.round(area * 100.0) / 100.0;
    }
}

Explanation:
The function takes three double arguments representing the lengths of the sides of a triangle.
It first checks if the three sides form a valid triangle by using the triangle inequality theorem.
If they don't form a valid triangle, it returns -1.
If they do form a valid triangle, it calculates the semi-perimeter of the triangle using the formula (s = (a+b+c)/2)
Then it calculates the area of the triangle using Heron's formula and returns the result rounded to two decimal points.
This is achieved by multiplying the area by 100.0, rounding to the nearest integer, then dividing by 100.0 to get the result in the correct decimal place.

*/

public class Main
{
    public static void main(String[] args)
    {
        Solution solution = new Solution();
        System.out.println(solution.triangleArea(3, 4, 5)); // 6.0
        System.out.println(solution.triangleArea(1, 2, 10)); // -1.0
    }
}

// This code will output:
// 6.0
// -1.0
// Which is the expected output.

```

The given Java code is a solution to the problem described in the problem statement. It checks if the three sides form a valid triangle and if so, it calculates and returns the area of the triangle, rounded to two decimal places. If the sides do not form a valid triangle, it returns -1.

This code uses the Heron's formula to calculate the area of a triangle given the lengths of its three sides. The formula is based on the semi-perimeter of the triangle, which is calculated as half the sum of the lengths of the sides. The area