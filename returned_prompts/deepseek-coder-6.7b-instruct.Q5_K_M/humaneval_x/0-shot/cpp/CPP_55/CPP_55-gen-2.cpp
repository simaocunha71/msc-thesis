    if(n<=1){
        return n;
    }
    else{
        return fib(n-1) + fib(n-2);
    }
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("Fibonacci number is: %d", fib(n));
    return 0;
}

// --------------------------------------

