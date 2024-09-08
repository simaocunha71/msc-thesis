    return (a*h)/2.0;
}
int main()
{
    float a,h;
    printf("Enter the length of a side:");
    scanf("%f",&a);
    printf("Enter the height:");
    scanf("%f",&h);
    printf("The area of the triangle is: %f",triangle_area(a,h));
    return 0;
}
