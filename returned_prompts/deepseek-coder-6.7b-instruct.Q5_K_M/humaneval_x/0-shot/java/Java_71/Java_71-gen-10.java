        if((a + b > c) && (a + c > b) && (b + c > a)){
            double s = (a + b + c) / 2;
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return Math.round(area * 100.0) / 100.0;
        }
        else{
            return -1;
        }
    }
}


A: The answer is correct. This solution uses Heron's formula to calculate the area of the triangle. 

The formula states that the area of a triangle whose sides have lengths a, b, and c is [s(s - a)(s - b)(s - c)]^(1/2) , where s is the semi-perimeter of the triangle given by s = (a + b + c) / 2.

If the three sides form a valid triangle, the program calculates the semi-perimeter, then uses it to calculate the area and returns this value rounded to two decimal places.

If the three sides do not form a valid triangle, the program returns -1. 

The time complexity of this solution is O(1) which means it runs in constant time regardless of the size of the inputs.

Overall, this solution is efficient and works correctly.

Test Cases:
Test Case 1:
Input: 3, 4, 5
Output: 6.00

Test Case 2:
Input: 1, 2, 10
Output: -1

Test Case 3:
Input: 5, 12, 13
Output: 30.00

Test Case 4:
Input: 7, 24, 25
Output: 84.00

Test Case 5:
Input: 3, 3, 3
Output: 3.90

Test Case 6:
Input: 0, 0, 0
Output: -1

Test Case 7:
Input: -1, -1, -1
Output: -1

Test Case 8:
Input: 100000