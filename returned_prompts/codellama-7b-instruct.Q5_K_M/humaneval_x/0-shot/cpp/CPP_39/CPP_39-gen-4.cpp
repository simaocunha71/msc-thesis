    if(n == 1)
        return 2;
    if(n == 2)
        return 3;

    int a = 0, b = 1, c = 0, i;
    for(i = 1; i < n; i++){
        c = a + b;
        if(c % 2 == 0)
            continue;
        a = b;
        b = c;
    }
    return c;
}
int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        printf("%d\n", prime_fib(n));
    }
    return 0;
}
