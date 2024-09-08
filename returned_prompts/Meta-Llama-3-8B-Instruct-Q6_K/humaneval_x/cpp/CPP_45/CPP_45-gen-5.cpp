    float s = (a*h)/2;
    return s;
}

int main() {
    float a, h;
    printf("Enter the length of a side: ");
    scanf("%f", &a);
    printf("Enter the height of a triangle: ");
    scanf("%f", &h);
    printf("The area of the triangle is: %f\n", triangle_area(a, h));
    return 0;
}
