    int fib4[5] = {0,0,2,0,0};
    for(int i = 5; i <= n; i++){
        int sum = fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4];
        fib4[i] = sum;
    }
    return fib4[n];
}

int main(){
    printf("%d\n",fib4(5));
    printf("%d\n",fib4(6));
    printf("%d\n",fib4(7));
    return 0;
}

