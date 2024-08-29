    float s;
    float area;
    s=(a+h)/2;
    area=sqrt(s*(s-a)*(s-h)*(s-a));
    return area;
}
int main(){
    float a,h,area;
    printf("Enter the length of side and height of triangle: ");
    scanf("%f%f",&a,&h);
    area=triangle_area(a,h);
    printf("The area of triangle is: %f",area);
    return 0;
}

