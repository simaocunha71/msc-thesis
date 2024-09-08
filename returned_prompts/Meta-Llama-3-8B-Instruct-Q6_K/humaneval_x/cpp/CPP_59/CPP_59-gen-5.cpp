    int max_prime=0;
    for(int i=2; i<=n; i++){
        if(n%i == 0){
            int is_prime = 1;
            for(int j=2; j*j<=i; j++){
                if(i%j == 0){
                    is_prime = 0;
                    break;
                }
            }
            if(is_prime){
                max_prime = i;
            }
        }
    }
    return max_prime;
}

int main(){
    printf("%d", largest_prime_factor(13195));
    return 0;
}
C:
#include <stdio.h>

int largest_prime_factor(int n) {
    int max_prime = 1;
    for (int i = 2; i <= n; i++) {
        if (n % i == 0) {
            int is_prime = 1;
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    is_prime = 0;
                    break;
                }
            }
            if (is_prime) {
                max_prime = i;
            }
        }
    }
    return max_prime;
}

int main() {
    printf("%d", largest_prime_factor(13195));
    return 0;
}