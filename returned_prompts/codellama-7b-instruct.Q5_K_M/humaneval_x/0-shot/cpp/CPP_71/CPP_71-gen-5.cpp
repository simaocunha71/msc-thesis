    if (a+b < c || b+c < a || c+a < b)
        return -1;
    float p = (a+b+c)/2;
    float area = sqrt(p*(p-a)*(p-b)*(p-c));
    return round(area*100)/100;
}
int main(){
    float a,b,c;
    printf("Enter three sides of the triangle: ");
    scanf("%f%f%f",&a,&b,&c);
    float area = triangle_area(a,b,c);
    printf("Area of the triangle is: %.2f\n",area);
    return 0;
}

Ans: *
