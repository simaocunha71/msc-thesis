    return 0;
}
int main(){
    float length,height,area;
    printf("Enter length of a side:");
    scanf("%f",&length);
    printf("Enter the height:");
    scanf("%f",&height);
    area=triangle_area(length,height);
    printf("The area of the triangle is %f",area);
    return 0;
}
