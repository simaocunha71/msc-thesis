    if(n==0) return 1;
    if(n%2==0){
        int temp=modp(n/2,p);
        return (temp*temp)%p;
    }
    else{
        int temp=modp((n-1)/2,p);
        return (((temp*temp)%p)*p)%p;
    }
}
int main()
{
    int n,p;
    printf("Enter the value of n and p : ");
    scanf("%d %d",&n,&p);
    printf("%d\n",modp(n,p));
    return 0;
}

