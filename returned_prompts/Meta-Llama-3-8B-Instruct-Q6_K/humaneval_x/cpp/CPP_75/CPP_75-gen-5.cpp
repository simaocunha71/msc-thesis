    // Here is my code
    bool is_prime[100] = {false};
    is_prime[0] = is_prime[1] = true;
    for(int i = 2; i < 100; i++) {
        if (!is_prime[i]) {
            for(int j = i; j < 100; j += i) {
                is_prime[j] = true;
            }
        }
    }
    for(int i = 2; i < 100; i++) {
        if (!is_prime[i]) {
            for(int j = i; j < 100; j += i) {
                is_prime[j] = true;
            }
        }
    }
    for(int i = 2; i < 100; i++) {
        if (!is_prime[i]) {
            for(int j = i; j < 100; j += i) {
                is_prime[j] = true;
            }
        }
    }
    int count = 0;
    for(int i = 2; i < 100; i++) {
        if (!is_prime[i]) {
            if (a%i == 0) {
                a /= i;
                count++;
                if (count == 3) return true;
            }
        }
    }
    return false;
}

int main() {
    printf("%d\n",is_multiply_prime(30)); // Should return 1
    return 0;
}
B:
    Here is the corrected version of the code:
    ```cpp
    #include <iostream>
    using namespace std;

    bool is_multiply_prime(int a) {
        for (int i = 2; i <= 100; i++) {
            for (int j = i; j <= 100; j++) {
                for (int k = j; k <= 100; k++) {
                    if (i * j * k == a) {
                        if (is_prime(i) && is_prime(j) && is_prime(k)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    bool is_prime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    int main() {
        cout << is_multiply_prime(30)