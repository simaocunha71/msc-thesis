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







C is the correct answer.

In C, the for loop is used to iterate from 1 to n and add each number to the sum. This will give the correct sum of all numbers from 1 to n.