    int fib[n];
    fib[0] = 2;
    fib[1] = 3;
    int i = 2;
    int j = 2;
    int k = 3;
    while(i<n){
        if(j%2==0 && j%3==0 && j%5==0 && j%7==0 && j%11==0 && j%13==0){
            fib[i] = j;
            i++;
        }
        j = k;
        k = j+k;
    }
    return fib[n-1];
}

