    if(n % 2 != 0){
        return false;
    }
    for(int i = 2; i <= n/2; i += 2){
        if(i % 2 == 0){
            int sum = i;
            for(int j = i+2; j <= n/2; j += 2){
                sum += j;
                if(sum == n){
                    return true;
                }
            }
        }
    }
    return false;
}

// Test Cases:
int main() {
    printf("%d\n", is_equal_to_sum_even(4));
    printf("%d\n", is_equal_to_sum_even(6));
    printf("%d\n", is_equal_to_sum_even(8));
    return 0;
}

*/
#include<stdio.h>

bool is_equal_to_sum_even(int n) {
    if (n % 2 != 0) {
        return false;
    }
    for (int i = 2; i <= n/2; i += 2) {
        int sum = i;
        for (int j = i+2; j <= n/2; j += 2) {
            sum += j;
            if (sum == n) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    printf("%d\n", is_equal_to_sum_even(4));
    printf("%d\n", is_equal_to_sum_even(6));
    printf("%d\n", is_equal_to_sum_even(8));
    return 0;
}




*/





































































































