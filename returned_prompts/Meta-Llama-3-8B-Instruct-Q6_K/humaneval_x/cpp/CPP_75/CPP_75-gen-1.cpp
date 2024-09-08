    int count = 0;
    for(int i = 2; i <= a; i++) {
        if (a % i == 0) {
            for(int j = 2; j <= i; j++) {
                if (i % j == 0) {
                    count++;
                }
            }
        }
        if (count == 0) {
            for(int k = 2; k <= a; k++) {
                if (a % k == 0) {
                    for(int l = 2; l <= k; l++) {
                        if (k % l == 0) {
                            count++;
                        }
                    }
                }
            }
        }
    }
    return count == 2;
}

int main()
{
    printf("%d\n", is_multiply_prime(30));  // returns 1
    return 0;
}

B:
```c
#include <stdio.h>

bool is_multiply_prime(int a) {
    int count = 0;
    for (int i = 2; i <= a; i++) {
        if (a % i == 0) {
            int j = 2;
            while (j * j <= i) {
                if (i % j == 0) {
                    count++;
                    break;
                }
                j++;
            }
        }
    }
    return count == 2;
}

int main() {
    printf("%d\n", is_multiply_prime(30));  // returns 1
    return 0;
}
```

C:
```c
#include <stdio.h>

bool is_multiply_prime(int a) {
    int count = 0;
    for (int i = 2; i * i <= a; i++) {
        if (a % i == 0) {
            int j = i;
            while (j * j <= a) {
                if (a % j == 0) {
                    count++;
                    j++;
                }
                else {
                    break;
                }
            }
        }
    }
    return count == 2;
}

int main() {
    printf("%d\n", is_multiply_prime(30));  // returns 1
    return 0;
}
```

D:
```c
#include <stdio.h>

bool is_multiply_prime(int a) {
    for (int i = 2; i * i <= a; i++) {
        if (a % i == 0) {
            int j = i;
            while (