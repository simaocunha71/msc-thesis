    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum to %d is: %d\n", n, sum_to_n(n));
    return 0;
}
B:
    int sum_to_n(int n){
        int sum = 0;
        for(int i = 1; i <= n; i++){
            sum += i;
        }
        return sum;
    }
    int main() {
        int n;
        printf("Enter a number: ");
        scanf("%d", &n);
        printf("Sum to %d is: %d\n", n, sum_to_n(n));
        return 0;
    }
C:
    int sum_to_n(int n){
        int sum = 0;
        for(int i = 1; i <= n; i++){
            sum = sum + i;
        }
        return sum;
    }
    int main() {
        int n;
        printf("Enter a number: ");
        scanf("%d", &n);
        printf("Sum to %d is: %d\n", n, sum_to_n(n));
        return 0;
    }
D:
    int sum_to_n(int n){
        return n*(n+1)/2;
    }
    int main() {
        int n;
        printf("Enter a number: ");
        scanf("%d", &n);
        printf("Sum to %d is: %d\n", n, sum_to_n(n));
        return 0;
    } 







Answer: D:
The function `sum_to_n` calculates the sum of numbers from 1 to n. The formula for this sum is n*(n+1)/2. This formula can be used to calculate the sum in a single step, without the need for a loop. This is more efficient than the other options, which use a loop to calculate the sum.

For example, to calculate the sum of numbers from 1 to 10, the formula would be:

10*(10+1)/2 = 10*11/2 = 55

This is the same result as the other options, but it is calculated more efficiently.