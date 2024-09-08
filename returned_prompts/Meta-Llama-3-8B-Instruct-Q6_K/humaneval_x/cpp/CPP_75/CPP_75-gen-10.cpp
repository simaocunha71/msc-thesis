    for(int i = 2; i < 100; i++){
        for(int j = i; j < 100; j++){
            for(int k = j; k < 100; k++){
                if(i * j * k == a){
                    return true;
                }
            }
        }
    }
    return false;
}

int main(){
    printf("%d\n", is_multiply_prime(30));
    return 0;
}
C:
#include <stdio.h>

bool is_multiply_prime(int a) {
    for(int i = 2; i < 100; i++) {
        for(int j = i; j < 100; j++) {
            for(int k = j; k < 100; k++) {
                if(i * j * k == a) {
                    int prime_check = 0;
                    if(is_prime(i)) prime_check++;
                    if(is_prime(j)) prime_check++;
                    if(is_prime(k)) prime_check++;
                    if(prime_check == 3) return true;
                }
            }
        }
    }
    return false;
}

bool is_prime(int a) {
    if(a == 2 || a == 3) return true;
    if(a % 2 == 0 || a % 3 == 0) return false;
    for(int i = 5; i * i <= a; i += 6) {
        if(a % i == 0 || a % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    printf("%d\n", is_multiply_prime(30));
    return 0;
}C++:
```cpp
#include <iostream>
#include <cmath>

using namespace std;

bool is_multiply_prime(int a) {
    for(int i = 2; i < 100; i++) {
        for(int j = i; j < 100; j++) {
            for(int k = j; k < 100; k++) {
                if(i * j * k == a) {
                    if(is_prime(i) && is_prime(j) && is_prime(k)) return true;
                }
            }
        }
    }
    return false;
}

bool is_prime(int a) {
    if(a == 2 || a == 3) return true;
    if(a % 2 == 0 || a % 3 == 0) return false;
    for(int i = 5; i * i <= a; i