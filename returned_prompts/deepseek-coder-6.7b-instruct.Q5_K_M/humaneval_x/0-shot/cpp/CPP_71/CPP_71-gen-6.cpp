if (a+b>c && a+c>b && b+c>a)
{
    float s = (a+b+c)/2;
    float area = sqrt(s*(s-a)*(s-b)*(s-c));
    return roundf(area * 100) / 100;
}
else
{
    return -1;
}
}
int main(){
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    float result = triangle_area(a,b,c);
    if(result == -1){
        printf("Invalid sides");
    }
    else{
        printf("Area of triangle is %.2f",result);
    }
    return 0;
}
//Pseudocode
BEGIN
FUNCTION triangle_area(a, b, c)
  IF (a + b > c AND a + c > b AND b + c > a)
    THEN
    s = (a + b + c) / 2
    area = SQRT(s * (s - a) * (s - b) * (s - c))
    RETURN ROUND(area * 100) / 100
  ELSE
    RETURN -1
  ENDIF
END FUNCTION
BEGIN
  READ a, b, c
  result = triangle_area(a, b, c)
  IF (result == -1)
    THEN
    PRINT "Invalid sides"
  ELSE
    PRINT "Area of triangle is ", result
  ENDIF
END
*/

```

This program takes the lengths of the sides of a triangle as inputs and checks if they form a valid triangle. If the sides form a valid triangle, it calculates the area of the triangle and rounds it to 2 decimal places. If the sides do not form a valid triangle, it returns -1.

The pseudocode for the program is as follows:

1. Define a function `triangle_area(a, b, c)` that takes the lengths of the sides of a triangle as inputs.
2. If the sum of any two sides is greater