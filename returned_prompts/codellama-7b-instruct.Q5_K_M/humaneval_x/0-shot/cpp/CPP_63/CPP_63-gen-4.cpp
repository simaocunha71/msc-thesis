    if(n <= 1)
        return 0;
    if(n == 2)
        return 1;
    int a = fibfib(n-1);
    int b = fibfib(n-2);
    int c = fibfib(n-3);
    int d = a + b + c;
    return d;
}

int main(){
    int n = 8;
    printf("fibfib(%d) == %d\n", n, fibfib(n));
    return 0;
}

