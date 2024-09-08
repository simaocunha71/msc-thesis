    vector<int> res(n);
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            res[i-1] = i * fact(i);  // Calculate factorial
        } else {
            int sum = 0;
            for (int j = 1; j <= i; j++) {
                sum += j;
            }
            res[i-1] = sum;  // Calculate sum of numbers from 1 to i
        }
    }
    return res;
}

int fact(int n) {
    int res = 1;
    for (int i = 2; i <= n; i++) {
        res *= i;
    }
    return res;
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    vector<int> result = f(n);
    for (int i = 0; i < n; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

C:
#include <stdio.h>
#include <stdlib.h>

int f(int n, int *res) {
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            res[i-1] = i * fact(i);
        } else {
            int sum = 0;
            for (int j = 1; j <= i; j++) {
                sum += j;
            }
            res[i-1] = sum;
        }
    }
    return 0;
}

int fact(int n) {
    int res = 1;
    for (int i = 2; i <= n; i++) {
        res *= i;
    }
    return res;
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    int *res = (int *)malloc(sizeof(int) * n);
    f(n, res);
    for (int i = 0; i < n; i++) {
        printf("%d ", res[i]);
    }
    printf("\n");
    free(res);
    return 0;
}  // Corrected C code

