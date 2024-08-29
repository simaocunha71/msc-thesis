#include <iostream>
using namespace std;

bool is_multiply_prime(int n) {
    if (n < 2) return false;
    int count = 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
            }
            if (i > 1) count++;
            if (count > 3) return false;
        }
    }
    if (n > 1) count++;
    return count == 3;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_prime(num)) {
        cout << num << " is a multiplication of 3 prime numbers." << endl;
    } else {
        cout << num << " is not a multiplication of 3 prime numbers." << endl;
    }
    return 0;
}
B:
#include <iostream>
#include <vector>

using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool is_multiply_prime(int n) {
    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (is_prime(i)) {
            primes.push_back(i);
            if (primes.size() == 3) break;
        }
    }
    int product = 1;
    for (int i = 0; i < 3; i++) {
        product *= primes[i];
    }
    return product == n;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_prime(num)) {
        cout << num << " is a multiplication of 3 prime numbers." << endl;
    } else {
        cout << num << " is not a multiplication of 3 prime numbers." << endl;
    }
    return 0;
}
C:
#include <iostream>
#include <vector>

using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 