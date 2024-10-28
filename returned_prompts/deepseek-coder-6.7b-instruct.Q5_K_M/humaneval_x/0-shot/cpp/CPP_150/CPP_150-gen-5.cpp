    int i;
    for (i=2; i<=n/2; ++i) {
        if (n%i == 0) {
            return y;
        }
    }

    return x;
}

int main() {
    printf("%d ", x_or_y(7, 34, 12));
    printf("%d ", x_or_y(15, 8, 5));
    return 0;
}

*/

#include <stdio.h>

int is_prime(int n) {
    if (n <= 1) return 0;
    if (n % 2 == 0 && n > 2) return 0;
    for(int i = 3; i * i <= n; i += 2) {
        if(n % i == 0)
            return 0;
    }
    return 1;
}

int x_or_y(int n, int x, int y) {
    return (is_prime(n)) ? x : y;
}

int main() {
    printf("%d ", x_or_y(7, 34, 12));
    printf("%d ", x_or_y(15, 8, 5));
    return 0;
}

*/











































































































































































































