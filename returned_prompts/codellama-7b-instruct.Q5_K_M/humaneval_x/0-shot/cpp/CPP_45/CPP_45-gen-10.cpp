    return sqrt(0.5*h*a);
}
int main(){
    float a,h;
    scanf("%f%f",&a,&h);
    printf("%.2f",triangle_area(a,h));
    return 0;
}
