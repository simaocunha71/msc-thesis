    if(a+b>c && a+c>b && b+c>a) {
        float s = (a+b+c)/2;
        return round(sqrt(s*(s-a)*(s-b)*(s-c))*100.0)/100.0;
    }
    else return -1.0;
}  // 100.0 is used to get 2 decimal places
// round is used to round off the answer to 2 decimal places
// round(sqrt(s*(s-a)*(s-b)*(s-c))*100.0)/100.0; is used to round off the answer to 2 decimal places
// round(sqrt(s*(s-a)*(s-b)*(s-c))*100.0)/100.0 is used to get the area of the triangle
// The function returns -1.0 if the sides do not form a triangle
// The formula for the area of a triangle is (sqrt(s*(s-a)*(s-b)*(s-c))) where s is the semi-perimeter of the triangle 
// The formula for the semi-perimeter is (a+b+c)/2 
// The formula for the area of a triangle is used to calculate the area of the triangle.  // 
// The area is then rounded off to 2 decimal places. 
// The function returns -1.0 if the sides do not form a triangle. 
// The sides form a triangle if the sum of any two sides is greater than the third side. 
// This is checked in the if statement before calculating the area. 
// The if statement checks if the sum of any two sides is greater than the third side. 
// If the sum of any two sides is greater than the third side, the sides form a triangle. 
// If the sum of any two sides is not greater than the third side, the sides do not form a triangle. 
// In this case, the function returns -1.0. 
// The function uses the formula for the area of a triangle to calculate the area of the triangle. 
// The formula for the area of a triangle is used to calculate the area of the triangle. 
// The area is then rounded off to 2 decimal places. 
// The function returns -1.0 if the sides do not form a triangle. 
// The sides form a triangle if the sum of any two sides is greater than the third side. 
// This is checked in the if statement before calculating the area. 
// The if statement checks if the sum of any two