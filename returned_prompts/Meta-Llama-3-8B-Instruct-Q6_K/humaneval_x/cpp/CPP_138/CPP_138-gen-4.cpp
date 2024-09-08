    for(int i = 2; i <= n; i += 2){
        int sum = 0;
        for(int j = 2; j <= n; j += 2){
            sum += j;
            if(sum == n) return true;
            if(sum > n) break;
        }
    }
    return false;
}

int main() {
    printf("%d\n", is_equal_to_sum_even(8));  // return 1
    return 0;
}
B:
#include <stdio.h>

bool is_equal_to_sum_even(int n) {
    for (int i = 2; i <= n; i += 2) {
        int sum = 0;
        for (int j = 2; j <= n; j += 2) {
            sum += j;
            if (sum == n) {
                return true;
            }
            if (sum > n) {
                break;
            }
        }
    }
    return false;
}

int main() {
    printf("%d\n", is_equal_to_sum_even(8));  // return 1
    return 0;
}

C:
#include <stdio.h>

bool is_equal_to_sum_even(int n) {
    for (int i = 2; i <= n; i += 2) {
        int sum = 0;
        for (int j = 2; j <= n; j += 2) {
            sum += j;
            if (sum == n) {
                return true;
            }
            if (sum > n) {
                break;
            }
        }
    }
    return false;
}

int main() {
    printf("%d\n", is_equal_to_sum_even(8));  // return 1
    return 0;
}

D:
#include <stdio.h>

bool is_equal_to_sum_even(int n) {
    for (int i = 2; i <= n; i += 2) {
        int sum = 0;
        for (int j = 2; j <= n; j += 2) {
            sum += j;
            if (sum == n) {
                return true;
            }
            if (sum > n) {
                break;
            }
        }
    }
    return false;
}

int main() {
    printf("%d\n", is_equal_to_sum_even(8));  // return 1
    return 0;
}

E:
#include <stdio.h>

bool is_equal_to