    return 0.5*a*h;

}
int main() {
    float a,h;
    printf("Enter the length of the side :");
    scanf("%f",&a);
    printf("Enter the height of the triangle :");
    scanf("%f",&h);
    printf("The area of the triangle is :%.2f",triangle_area(a,h));
    return 0;
}
