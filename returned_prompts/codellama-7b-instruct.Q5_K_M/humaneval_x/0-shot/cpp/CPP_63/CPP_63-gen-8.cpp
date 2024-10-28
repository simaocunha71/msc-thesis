    if(n<=1)
        return n;
    int a=fibfib(n-1);
    int b=fibfib(n-2);
    int c=fibfib(n-3);
    return a+b+c;
}
int main(){
    printf("%d",fibfib(8));
    return 0;
}
