    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}
int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("Sum of numbers from 1 to %d: %d\n", n, sum_to_n(n));
    return 0;
}
B:
    int sum_to_n(int n){
        return n * (n + 1) / 2;
    }
    int main(){
        int n;
        printf("Enter the number: ");
        scanf("%d", &n);
        printf("Sum of numbers from 1 to %d: %d\n", n, sum_to_n(n));
        return 0;
    }
C:
    int sum_to_n(int n){
        return n;
    }
    int main(){
        int n;
        printf("Enter the number: ");
        scanf("%d", &n);
        printf("Sum of numbers from 1 to %d: %d\n", n, sum_to_n(n));
        return 0;
    }
D:
    int sum_to_n(int n){
        return 0;
    }
    int main(){
        int n;
        printf("Enter the number: ");
        scanf("%d", &n);
        printf("Sum of numbers from 1 to %d: %d\n", n, sum_to_n(n));
        return 0;
    }

Correct Answer: B

Explanation: The sum of the numbers from 1 to n is given by the formula n*(n+1)/2. This is because the sum of the first n natural numbers is equal to the sum of the first n odd numbers, which is n^2. The sum of the first n even numbers is n*(n+1). Therefore, the sum of the first n natural numbers is n*(n+1)/2. This formula is used in the sum_to_n function in option B. The other options are incorrect because they do not use the correct formula or they do not handle the case where n is 0. Option A uses a for loop to calculate the sum, which is correct but less efficient than using the formula. Option C returns the value of n, which is incorrect because it does not calculate the sum of the numbers from 1 to n. Option D returns 0, which is incorrect because it does not calculate the sum of the numbers from