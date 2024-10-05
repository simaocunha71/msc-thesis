    if (n == 0)
        return 0;
    else if (n == 1)
        return 0;
    else if (n == 2)
        return 1;
    else
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3);
}

int main(){
    int n;
    printf("Enter the value of n\n");
    scanf("%d", &n);
    printf("The nth value of fibfib is %d\n", fibfib(n));
    return 0;
}


