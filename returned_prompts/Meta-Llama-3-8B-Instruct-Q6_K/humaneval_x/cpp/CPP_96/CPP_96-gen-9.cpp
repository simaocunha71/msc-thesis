    vector<int> primes;
    for (int i = 2; i < n; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push_back(i);
        }
    }
    return primes;
}

int main() {
    printf("%lu\n", count_up_to(5).size()); // 2
    printf("%lu\n", count_up_to(11).size()); // 4
    printf("%lu\n", count_up_to(0).size()); // 0
    printf("%lu\n", count_up_to(20).size()); // 8
    printf("%lu\n", count_up_to(1).size()); // 0
    printf("%lu\n", count_up_to(18).size()); // 8
    return 0;
}
B:
    vector<int> count_up_to(int n) {
        vector<int> primes;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primes.push_back(i);
            }
        }
        return primes;
    }

    bool isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    int main() {
        printf("%lu\n", count_up_to(5).size()); // 2
        printf("%lu\n", count_up_to(11).size()); // 4
        printf("%lu\n", count_up_to(0).size()); // 0
        printf("%lu\n", count_up_to(20).size()); // 8
        printf("%lu\n", count_up_to(1).size()); // 0
        printf("%lu\n", count_up_to(18).size()); // 8
        return 0;
    }
C:
    #include<bits/stdc++.h>
    #include<vector>
    using namespace std;

    vector<int> count_up_to(int n) {
        vector<int> primes;
        for (int i = 2; i < n; i++) {
            bool is