    if (n <= 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fib(n-1) + fib(n-2);
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("%dth Fibonacci number is: %d",n,fib(n));
    return 0;
}

*/



//


/*
