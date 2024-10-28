
return (a*b*c)/2;
}
int main()
{
    float a,b,c;
    cin>>a>>b>>c;
    if(a+b>c)
    {
        printf("%.2f",triangle_area(a,b,c));
    }
    else{
        printf("-1");
    }
    return 0;
}
