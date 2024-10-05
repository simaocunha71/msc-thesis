        if(a + b <= c || a + c <= b || b + c <= a)
            return -1;
        else
        {
            double s = (a + b + c) / 2;
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return Math.round(area * 100.0) / 100.0;
        }
    }
}

This solution first checks if the given sides can form a valid triangle. If not, it returns -1. If they can form a valid triangle, it then calculates the semi-perimeter of the triangle, and finally the area using Heron's formula.
*/

class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Solution sol = new Solution();
        System.out.println(sol.triangleArea(3, 4, 5)); // Expected output: 6.00
        System.out.println(sol.triangleArea(1, 2, 10)); // Expected output: -1
    }
}

/*
Test cases:
Input: 3, 4, 5
Output: 6.00

Input: 1, 2, 10
Output: -1

Input: 5, 12, 13
Output: 30.00

This solution will pass these test cases.
*/