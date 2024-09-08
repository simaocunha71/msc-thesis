#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 0 || n == 0) {
        return false;
    }
    double log_result = log(x) / log(n);
    if (log_result == floor(log_result)) {
        return true;
    }
    return false;
}

int main() {
    printf("%d\n", is_simple_power(1, 4)); // true
    printf("%d\n", is_simple_power(2, 2)); // true
    printf("%d\n", is_simple_power(8, 2)); // true
    printf("%d\n", is_simple_power(3, 2)); // false
    printf("%d\n", is_simple_power(3, 1)); // false
    printf("%d\n", is_simple_power(5, 3)); // false
    return 0;
}

C:
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 0 || n == 0) {
        return false;
    }
    double log_result = log(x) / log(n);
    if (log_result == floor(log_result)) {
        return true;
    }
    return false;
}

int main() {
    printf("%d\n", is_simple_power(1, 4)); // true
    printf("%d\n", is_simple_power(2, 2)); // true
    printf("%d\n", is_simple_power(8, 2)); // true
    printf("%d\n", is_simple_power(3, 2)); // false
    printf("%d\n", is_simple_power(3, 1)); // false
    printf("%d\n", is_simple_power(5, 3)); // false
    return 0;
}

D:
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_simple_power(int x, int n) {
    if (x == 0 || n == 0) {
        return false;
    }
    double log_result = log(x) / log(n);
    if (log_result == floor(log_result)) {
        return true;
    }
    return false;
}

int main() {
    printf("%d\n", is_simple_power(1, 4)); // true
    printf("%d\n", is_simple_power(