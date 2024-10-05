    // sort the sides in ascending order
    if (a > b) swap(a, b);
    if (a > c) swap(a, c);
    if (b > c) swap(b, c);

    // check if it forms a right-angled triangle
    return (c*c == a*a + b*b);
}


int main(){
    float a, b, c;
    scanf("%f %f %f",&a,&b,&c);
    bool ans = right_angle_triangle(a, b, c);
    printf("%d\n", ans);
    return 0;
}


