    if(n<1) return 0;
    if(n==1) return 0;
    if(n==2) return 1;
    int a=0,b=0,c=1;
    for(int i=3;i<=n;i++){
        int temp=a+b+c;
        a=b;
        b=c;
        c=temp;
    }
    return c;

}
int main()
{
    printf("%d",fibfib(8));
    return 0;
}
B:
    int fibfib(int n){
        if(n<1) return 0;
        if(n==1) return 0;
        int a=0,b=0,c=1;
        for(int i=3;i<=n;i++){
            int temp=a+b+c;
            a=b;
            b=c;
            c=temp;
        }
        return c;
    }
    int main()
    {
        printf("%d\n",fibfib(8));
        return 0;
    }
C:
    int fibfib(int n){
        if(n<1) return 0;
        if(n==1) return 0;
        if(n==2) return 1;
        int a=0,b=1,c=1;
        for(int i=3;i<=n;i++){
            int temp=a+b+c;
            a=b;
            b=c;
            c=temp;
        }
        return c;
    }
    int main()
    {
        printf("%d\n",fibfib(8));
        return 0;
    }
D:
    int fibfib(int n){
        if(n<1) return 0;
        if(n==1) return 0;
        if(n==2) return 1;
        if(n==3) return 2;
        int a=0,b=0,c=1,d=1;
        for(int i=4;i<=n;i++){
            int temp=a+b+c+d;
            a=b;
            b=c;
            c=d;
            d=temp;
        }
        return d;
    }
    int main()
    {
        printf("%d\n",fibfib(8));
        return 0;
    }
E:
    int fibfib(int n){
        if(n<1) return 0;
        if(n==1) return 0;
        if(n==2) return 1;
        int a=0,b=0,c=1;
        for(int i=3;i<=n;i++){
            int temp=a