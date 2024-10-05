    float s = (a+b+c)/2;
    if (a+b>c && a+c>b && b+c>a)
    {
        return round((sqrt(s*(s-a)*(s-b)*(s-c)))*100.0)/100.0;
    }
    else
    {
        return -1;
    }
} // end function triangle_area
// test the function
int main() {
    float a = 3.0;
    float b = 4.0;
    float c = 5.0;
    float result = triangle_area(a,b,c);
    printf("The area of the triangle with sides a=%f, b=%f, c=%f is %f\n", a, b, c, result);
    return 0;
} // end main


