    if(a<=100)
    {
        for(int i=2;i<a;i++)
        {
            if(a%i==0)
            {
                goto A;
            }
        }
    }
    else
    {
        return 0;
    }
    return 1;
}

int main()
{
    int a;
    scanf("%d",&a);
    printf("%d",is_multiply_prime(a));
    return 0;
}

