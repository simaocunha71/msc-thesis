    int f[4] = {0, 0, 2, 0};
    if(n<4) return f[n];
    int next;

B:
    for(int i=4; i<=n; i++){
        next = f[3] + f[2] + f[1] + f[0];
        f[0] = f[1];
        f[1] = f[2];
        f[2] = f[3];
        f[3] = next;
    }
    return next;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The %dth fib4 number is: %d", n, fib4(n));
    return 0;
}

*/

Here's the explanation of the code:

A: We initialize an array `f[]` with the first 4 numbers of the sequence. If `n` is smaller than 4, we return the corresponding element in the array.

B: We loop from 4 to `n` (inclusive), each time calculating the next number as the sum of the last 4 numbers in the sequence and updating the array `f[]`.

Finally, we return the `next` value, which is the n-th number in the sequence.

This solution uses a dynamic programming approach to avoid redundant computations by storing the computed values in an array. This makes the time complexity linear.
*/

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The %dth fib4 number is: %d", n, fib4(n));
    return 0;
}

int fib4(int n){
    int f[4] = {0, 0, 2, 0};
    if(n<4) return f[n];
    int next;
    for(int i=4; i<=n; i++){
        next = f[3] + f[2] + f[1] + f[0];
        f[0] = f[1];
        f[1]