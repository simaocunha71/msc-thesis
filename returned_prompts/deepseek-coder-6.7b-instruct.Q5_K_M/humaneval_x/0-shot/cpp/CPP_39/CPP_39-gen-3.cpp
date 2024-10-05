    int fib1 = 0, fib2 = 1, fib3, i, count = 2, prime = 2;
    if(n == 1)
        return 2;
    if(n == 2)
        return 3;
    while(count < n){
        fib3 = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib3;
        if(fib2 == prime){
            prime += 2;
            continue;
        }
        fib3 = prime;
        prime += 2;
        count++;
    }
    return fib3;
}
int main(){
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d-th Fibonacci Prime is: %d\n", n, prime_fib(n));
    return 0;
}

*/

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d-th Fibonacci Prime is: %d\n", n, prime_fib(n));
    return 0;
}


/*
int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d-th Fibonacci Prime is: %d\n", n, prime_fib(n));
    return 0;
}
*/


/*
int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d-th Fibonacci Prime is: %d\n", n, prime_fib(n));
    return 0;
}
*/


/*
int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("%d-th Fibonacci Prime is: %d\n", n, prime_fib(n));
    return 0;
}
*/



/*
int main() {
    int n;
    printf("Enter n: ");
    scan