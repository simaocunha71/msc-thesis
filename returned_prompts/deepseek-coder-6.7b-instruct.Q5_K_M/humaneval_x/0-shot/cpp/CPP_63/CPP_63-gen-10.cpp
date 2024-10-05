    if (n == 0 || n == 1) {
        return 0;
    }
    else if (n == 2) {
        return 1;
    }
    else {
        int fibfib_nums[n+1];
        fibfib_nums[0] = 0;
        fibfib_nums[1] = 0;
        fibfib_nums[2] = 1;
        for (int i = 3; i <= n; i++) {
            fibfib_nums[i] = fibfib_nums[i-1] + fibfib_nums[i-2] + fibfib_nums[i-3];
        }
        return fibfib_nums[n];
    }
}

int main(){
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));
    return 0;
}
*/


/*
