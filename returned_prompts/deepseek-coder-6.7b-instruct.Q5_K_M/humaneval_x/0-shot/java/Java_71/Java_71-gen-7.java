        if(a+b>c && b+c>a && c+a>b){
            double s = (a+b+c)/2;
            double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
            return Math.round(area*100.0)/100.0;
        } else {
            return -1;
        }
    }
}

The solution first checks if the inputs can form a valid triangle, then calculates the semi-perimeter and uses it to calculate the area. The area is then returned rounded to 2 decimal points. If the inputs do not form a valid triangle, -1 is returned.

This solution uses Heron's formula to calculate the area of a triangle given the lengths of the three sides. This formula is based on the semi-perimeter of the triangle and is used in many programming languages.

The formula for Heron's formula is:
Area = √[s(s - a)(s - b)(s - c)]
where a, b, c are the sides of the triangle and s is the semi-perimeter of the triangle, given by:
s = (a + b + c) / 2
 */

import java.lang.Math;

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.triangleArea(3, 4, 5)); // Expected output: 6.0
        System.out.println(solution.triangleArea(1, 2, 10)); // Expected output: -1.0
    }
}


This program will print the area of the triangle and -1 if the sides cannot form a valid triangle.

It's important to note that the output will be a double, so if the area is 6.00, it will be returned as 6.0.



































































