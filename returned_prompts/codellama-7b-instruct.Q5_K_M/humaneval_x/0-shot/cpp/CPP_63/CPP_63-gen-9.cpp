    if(n==0||n==1){
        return 0;
    }
    if(n==2){
        return 1;
    }
    int a=fibfib(n-1);
    int b=fibfib(n-2);
    int c=fibfib(n-3);
    return a+b+c;
}
int main(){
    int n;
    scanf("%d",&n);
    printf("%d",fibfib(n));
    return 0;
}
