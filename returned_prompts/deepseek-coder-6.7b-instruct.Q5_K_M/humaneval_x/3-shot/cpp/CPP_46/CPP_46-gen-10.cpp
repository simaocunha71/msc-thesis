    if(n == 0 || n == 1) return 0;
    if(n == 2) return 2;
    if(n == 3) return 0;
    int fib[4] = {0, 0, 2, 0};
    int sum = 2;
    for(int i = 4; i <= n; i++){
        int temp = sum;
        sum = fib[3] + fib[2] + fib[1] + fib[0];
        for(int j = 0; j < 3; j++) fib[j] = fib[j+1];
        fib[3] = temp;
    }
    return sum;
}

