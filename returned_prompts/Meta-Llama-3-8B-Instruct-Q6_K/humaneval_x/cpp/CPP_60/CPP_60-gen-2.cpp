    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    return sum;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The sum of numbers from 1 to %d is: %d\n", n, sum_to_n(n));
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

    int main(){
        int n;
        printf("Enter a number: ");
        scanf("%d", &n);
        printf("The sum of numbers from 1 to %d is: %d\n", n, sum_to_n(n));
        return 0;
    }

C:
    int sum_to_n(int n){
        int sum = 0;
        for(int i = 1; i <= n; i++){
            sum += i;
        }
        return sum;
    }

    int main(){
        int n;
        printf("Enter a number: ");
        scanf("%d", &n);
        printf("The sum of numbers from 1 to %d is: %d\n", n, sum_to_n(n));
        return 0;
    }

D:
    int sum_to_n(int n){
        int sum = 0;
        for(int i = 1; i <= n; i++){
            sum += i;
        }
        return sum;
    }

    int main(){
        int n;
        printf("Enter a number: ");
        scanf("%d", &n);
        printf("The sum of numbers from 1 to %d is: %d\n", n, sum_to_n(n));
        return 0;
    }

Correct Answer: B, C, D

Explanation:
The sum of the numbers from 1 to n is given by the formula n*(n+1)/2. This is the mathematical way to solve this problem. But for the problem statement, the function sum_to_n is expected to return the sum of numbers from 1 to n. This can be done using a for loop that adds each number from 1 to n to a variable. The function sum_to_n is implemented in options B, C, and D. The main function in options B, C, and D prompts the user to