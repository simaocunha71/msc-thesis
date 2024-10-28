    if(a>0&&b>0&&c>0){
        if(a+b>c&&b+c>a&&a+c>b){
            float s=(a+b+c)/2;
            return round(sqrt(s*(s-a)*(s-b)*(s-c)));
        }
    }
    return -1;
}
int main(){
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    printf("%f",triangle_area(a,b,c));
    return 0;
}

Ans:
int triangle_area(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) {
        return -1;
    }
    if (a + b > c && b + c > a && a + c > b) {
        return (a + b + c) / 2;
    }
    return -1;
}
