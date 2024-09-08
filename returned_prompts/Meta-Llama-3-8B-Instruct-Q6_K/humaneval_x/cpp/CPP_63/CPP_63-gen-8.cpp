    if(n<=1)
        return 0;
    if(n==2)
        return 1;
    int a=0,b=0,c=1;
    for(int i=3;i<=n;i++){
        int temp=a+b+c;
        a=b;
        b=c;
        c=temp;
    }
    return c;
}
int main(){
    int n;
    printf("Enter the value of n:\n");
    scanf("%d",&n);
    printf("The %d-th element of the fibfib sequence is: %d\n",n,fibfib(n));
    return 0;
}
