    if(n==0)
    {
        printf("Input must be a positive integer");
        goto A;
    }
    else if(n==1)
    {
        return 2;
    }
    else if(n==2)
    {
        return 3;
    }
    else if(n==3)
    {
        return 5;
    }
    else if(n==4)
    {
        return 13;
    }
    else if(n==5)
    {
        return 89;
    }
    else
    {
        int i,j;
        int fibo[n];
        fibo[0]=0;
        fibo[1]=1;
        for(i=2;i<n;i++)
        {
            fibo[i]=fibo[i-1]+fibo[i-2];
            j=2;
            while(j*j<=fibo[i])
            {
                if(fibo[i]%j==0)
                {
                    return prime_fib(n);
                }
                j++;
            }
        }
        return fibo[n-1];
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    printf("%d",prime_fib(n));
    return 0;
}
*/








































































































































































