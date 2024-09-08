    if(a+b>c && a+c>b && b+c>a)
    {
        float s = (a+b+c)/2.0;
        float area = sqrt(s*(s-a)*(s-b)*(s-c));
        return round(area*100.0)/100.0;
    }
    else
    {
        return -1.0;
    }
}

int main()
{
    printf("%f\n",triangle_area(3,4,5)); // should return 6.00
    printf("%f\n",triangle_area(1,2,10)); // should return -1
    return 0;
}
