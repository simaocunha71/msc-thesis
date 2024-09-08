    long long res = 1;
    for(int i = 1; i <= n; i++){
        res *= i;
        for(int j = 2; j <= i; j++){
            res *= j;
        }
    }
    return res;
}

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("The special factorial of %d is %lld\n", num, special_factorial(num));
    return 0;
}

