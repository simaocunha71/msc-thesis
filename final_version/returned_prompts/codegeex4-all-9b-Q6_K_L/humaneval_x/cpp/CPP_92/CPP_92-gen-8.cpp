    if(a+b==c||a+c==b||b+c==a)
        return true;
    else
        return false;
}
int main()
{
    float a,b,c;
    printf("Enter three numbers: ");
    scanf("%f %f %f",&a,&b,&c);

    if(a%1==0&&b%1==0&&c%1==0)
    {
        printf("any_int(%f, %f, %f) ➞ ",a,b,c);
        if(any_int(a,b,c))
            printf("true");
        else
            printf("false");
    }
    else
    {
        printf("any_int(%f, %f, %f) ➞ ",a,b,c);
        if(any_int(a,b,c))
            printf("true");
        else
            printf("false");
    }
    return 0;
}
*/
/*
1. Create a