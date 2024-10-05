if(a+b>c)
{
float s=(a+b+c)/2;
float area=(s*(s-a)*(s-b)*(s-c))/256;
return area;
}
else
{
return -1;
}
}
int main()
{
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    printf("%.2f",triangle_area(a,b,c));
}
