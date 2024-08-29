    if((a+b)<c || (a+c)<b || (b+c)<a)
    {
        return -1;
    }
    else
    {
        float s=(a+b+c)/2;
        float area=sqrt(s*(s-a)*(s-b)*(s-c));
        return area;
    }
}
int main(){
    float a,b,c;
    scanf("%f%f%f",&a,&b,&c);
    float area=triangle_area(a,b,c);
    printf("%f",area);
    return 0;
}
