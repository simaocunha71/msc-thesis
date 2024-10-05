    if(n<2){
        return 0;
    }
    else if(n==2){
        return 2;
    }
    else if(n==3){
        return 0;
    }
    else{
        int fib1=0,fib2=0,fib3=2,fib4=0;
        for(int i=4;i<=n;i++){
            int temp=fib4;
            fib4+=fib1;
            fib1=fib2;
            fib2=fib3;
            fib3=temp;
        }
        return fib4;
    }
}
int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d-th element of the fib4 sequence is: %d", n, fib4(n));
    return 0;
}
*/

#include <stdio.h>

int fib4(int n){
    if(n < 4){
        if(n < 0) return 0;
        return n;
    }
    int f1 = 0, f2 = 0, f3 = 2, f4 = 0, temp;
    for(int i = 4; i <= n; i++){
        temp = f4;
        f4 += f1;
        f1 = f2;
        f2 = f3;
        f3 = temp;
    }
    return f4;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d-th element of the fib4 sequence is: %d\n", n, fib4(n));
    return 0;
}
/*
int main() {
    printf("%d\n", fib4(5)); // 4
    printf("%d\n", fib4(6)); // 8
    printf("%d\n", fib4(7)); // 14
    return 0;
}
*/






















