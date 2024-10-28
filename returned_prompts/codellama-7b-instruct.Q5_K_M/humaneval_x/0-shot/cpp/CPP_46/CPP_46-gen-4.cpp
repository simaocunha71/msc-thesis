    if(n <= 1) return n;
    int a, b, c, d;
    a = 0; b = 0; c = 2; d = 0;
    for(int i=4; i<=n; i++){
        if(i == 4) goto A;
        d = a + b + c;
        a = b;
        b = c;
        c = d;
    }
    return d;
}

int main(){
    printf("%d\n", fib4(5));
    printf("%d\n", fib4(6));
    printf("%d\n", fib4(7));
    return 0;
}
