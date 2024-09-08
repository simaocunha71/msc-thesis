    if(p==0)
        return 1;
    if(n==0)
        return 1;

    if((n%p)==0)
        return modp(n/p,p);

    else
        return (modp(n/p,p)*(modp(1,p))) % p;
}
int main()
{
    int n,p;
    printf("Enter the value of n: ");
    scanf("%d",&n);
    printf("Enter the value of p: ");
    scanf("%d",&p);
    printf("The result is: %d\n",modp(n,p));
    return 0;
}
