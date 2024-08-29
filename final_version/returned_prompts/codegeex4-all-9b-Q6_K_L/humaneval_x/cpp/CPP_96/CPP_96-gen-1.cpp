#include <iostream>
#include <vector>
using namespace std;

bool is_prime(int num) {
    if (num <= 1)
        return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}

vector<int> count_up_to(int n) {
    vector<int> primes;
    for (int i = 2; i < n; i++) {
        if (is_prime(i))
            primes.push_back(i);
    }
    return primes;
}

int main() {
    int n;
    cout << "Enter a non-negative integer: ";
    cin >> n;
    vector<int> result = count_up_to(n);
    cout << "Primes less than " << n << ": ";
    for (int prime : result) {
        cout << prime << " ";
    }
    cout << endl;
    return 0;
}
