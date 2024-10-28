    if(n==1) return 0;
    if(n==2) return 1;
    if(n==3) return 1;
    if(n>3){
        int a = fibfib(n-1);
        int b = fibfib(n-2);
        int c = fibfib(n-3);
        return a + b + c;
    }
    goto A;
}
int main(){
    int n;
    scanf("%d", &n);
    int res = fibfib(n);
    printf("%d", res);
}

