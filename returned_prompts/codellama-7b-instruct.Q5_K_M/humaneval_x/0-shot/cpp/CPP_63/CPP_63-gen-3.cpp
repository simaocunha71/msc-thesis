
int fibfib(int n){
    if(n==0)
        return 0;
    else if(n==1)
        return 0;
    else if(n==2)
        return 1;
    else{
        int a=fibfib(n-1);
        int b=fibfib(n-2);
        int c=fibfib(n-3);
        return a+b+c;
    }
}
