    int fib4[100]; // Create an array to store the fib4 sequence
    fib4[0] = 0; // Base case 1
    fib4[1] = 0; // Base case 2
    fib4[2] = 2; // Base case 3
    fib4[3] = 0; // Base case 4

    for(int i = 4; i <= n; i++) {
        fib4[i] = fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4]; // Calculate the next element
    }
    return fib4[n];
}
int main() {
    printf("%d\n", fib4(5)); // Output: 4
    printf("%d\n", fib4(6)); // Output: 8
    printf("%d\n", fib4(7)); // Output: 14
    return 0;
}
int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The %d-th element of the fib4 number sequence is: %d\n", n, fib4(n));
    return 0;
}
