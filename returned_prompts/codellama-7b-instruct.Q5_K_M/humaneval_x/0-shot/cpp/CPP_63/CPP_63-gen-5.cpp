    if (n == 1 || n == 2)
        return 0;
    if (n == 3)
        return 1;
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3);
}

int main(){
    printf("%d", fibfib(8));
    return 0;
}


