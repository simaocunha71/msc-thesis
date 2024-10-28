The area of a triangle is given by the formula 
sqrt(s*(s-a)*(s-b)*(s-c)) 
where s is the semi-perimeter of the triangle and a, b, c are the lengths of the sides.

The area of a triangle is -1 if the three sides do not form a valid triangle. A triangle is valid if the sum of the lengths of any two sides is greater than the length of the third side.

So, in the function triangle_area, we first check if the three sides can form a valid triangle. If they can, we calculate the semi-perimeter s and then use the formula to calculate the area of the triangle. The area is then rounded to two decimal places using the round function. If the sides cannot form a valid triangle, we return -1.

The main function reads the lengths of the three sides of a triangle from the user, calls the triangle_area function with these lengths, and then prints the result. If the result is not -1, it prints the area of the triangle. Otherwise, it prints an error message.

The time complexity of this program is O(1) because it does a constant number of operations regardless of the input size. The space complexity is O(1) because it uses a constant amount of space to store the input and output values.

This program uses