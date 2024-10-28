    if(n%2==0)
    {
        n=n/2;
        goto A;
    }
    for(int i=3;i<=n;i=i+2)
    {
        if(n%i==0)
        {
            n=n/i;
            goto A;
        }
    }
    return n;
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    int lpf = largest_prime_factor(n);
    printf("%d",lpf);
}


