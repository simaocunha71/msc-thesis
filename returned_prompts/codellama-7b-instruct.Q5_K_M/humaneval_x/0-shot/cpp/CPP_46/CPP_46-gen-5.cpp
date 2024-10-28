    if (n == 0){
        return 0;
    }
    if (n == 1){
        return 0;
    }
    if (n == 2){
        return 2;
    }
    if (n == 3){
        return 0;
    }
    if (n > 3){
        n-=4;
        goto A;
    }
}

int main(void){
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d", fib4(n));
}
