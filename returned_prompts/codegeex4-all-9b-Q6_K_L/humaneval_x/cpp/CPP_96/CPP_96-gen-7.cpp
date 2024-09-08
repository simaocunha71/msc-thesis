```cpp
#include <iostream>
#include <vector>
using namespace std;

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}

vector<int> count_up_to(int n) {
    vector<int> result;
    for (int i = 2; i < n; i++) {
        if (is_prime(i)) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    vector<int> primes = count_up_to(n);
    cout << "Prime numbers less than " << n << ": ";
    for (int prime : primes) {
        cout << prime << " ";
    }
    cout << endl;
    return 0;
}
```