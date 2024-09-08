    if(n<=1)
        return n;
    else
        return fib(n-1) + fib(n-2);

}
int main(){

    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("The %d-th Fibonacci number is %d\n", n, fib(n));
    return 0;
}
B:
    int fib(int n){
        if(n <= 1)
            return n;
        int a = 0, b = 1, result = 0;
        for(int i = 2; i <= n; i++){
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
    int main(){
        int n;
        printf("Enter the number: ");
        scanf("%d", &n);
        printf("The %d-th Fibonacci number is %d\n", n, fib(n));
        return 0;
    }

C:
    int fib(int n){
        if(n <= 1)
            return n;
        int result = 0;
        int a = 0, b = 1;
        for(int i = 2; i <= n; i++){
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
    int main(){
        int n;
        printf("Enter the number: ");
        scanf("%d", &n);
        printf("The %d-th Fibonacci number is %d\n", n, fib(n));
        return 0;
    }

D:
    int fib(int n){
        if(n <= 1)
            return n;
        int result = 0;
        int a = 0, b = 1;
        for(int i = 2; i <= n; i++){
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
    int main(){
        int n;
        printf("Enter the number: ");
        scanf("%d", &n);
        printf("The %d-th Fibonacci number is %d\n", n, fib(n));
        return 0;
    }

Answer: B, C, D are all correct. They all compute the nth Fibonacci number using a loop. The main difference is that the loop variable `i` is declared inside the loop in option C and D, whereas it is declared outside the loop in option B. Both ways are