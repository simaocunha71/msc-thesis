    if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a)
        return true;
    else
        return false;
}
int main(){
    float a,b,c;
    printf("Enter the first side: ");
    scanf("%f",&a);
    printf("Enter the second side: ");
    scanf("%f",&b);
    printf("Enter the third side: ");
    scanf("%f",&c);
    if(right_angle_triangle(a,b,c))
        printf("The three sides form a right-angled triangle.\n");
    else
        printf("The three sides do not form a right-angled triangle.\n");
    return 0;
}

