    if(a+b<=c || b+c<=a || c+a<=b){
        return -1;
    }

    float s = (a+b+c)/2;
    float area = sqrt(s*(s-a)*(s-b)*(s-c));

    return roundf(area * 100) / 100;
}
int main() {
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    printf("%f\n",triangle_area(a,b,c));
    return 0;
}

// Code: Ends

// Solution: Starts
S:
The provided code takes three inputs a, b, and c which are the lengths of the sides of a triangle. The function triangle_area(a, b, c) calculates the area of the triangle if it's valid.

The function begins by checking if the triangle is valid. If the sum of any two sides is not greater than the third, the function returns -1.

If the triangle is valid, the function calculates the semi-perimeter of the triangle (s = (a+b+c)/2).

The formula to calculate the area of a triangle given the lengths of the three sides is sqrt(s*(s-a)*(s-b)*(s-c)). The function then calculates the area and returns it rounded to two decimal places using the roundf function.

Finally, the function returns the calculated area of the triangle. If the triangle is not valid, the function returns -1.

The main function reads the lengths of the sides of a triangle from the user, calls the triangle_area function with these lengths, and prints the returned value.

The main function returns 0 at the end.
// Solution: Ends

// Explanation: Starts
E:
This code is a solution to the given problem. It uses the formula for the area of a triangle given the lengths of the three sides. The code checks if the given sides can form a valid triangle and calculates the area accordingly. If the triangle is not valid, it returns -1. The area is rounded to 2 decimal places using the roundf function.