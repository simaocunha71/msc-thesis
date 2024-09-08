#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool is_multiply_prime(int a) {
    int count = 0;
    for (int i = 2; i <= a; i++) {
        if (is_prime(i) && a % i == 0) {
            count++;
            a /= i;
            i = 1; // reset i to 1 to start from 2 again
        }
    }
    return count == 3;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_prime(num)) {
        cout << num << " is the multiplication of 3 prime numbers." << endl;
    } else {
        cout << num << " is not the multiplication of 3 prime numbers." << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool is_multiply_prime(int a) {
    int count = 0;
    int prime_factors[3] = {0};
    for (int i = 2; i <= a; i++) {
        if (is_prime(i) && a % i == 0) {
            prime_factors[count++] = i;
            a /= i;
            if (count == 3) break;
            i = 1; // reset i to 1 to start from 2 again
        }
    }
    return count == 3 && prime_factors[0] * prime_factors[1] * prime_factors[2] == a;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_prime(num)) {
        cout << num << " is the multiplication of 3 prime numbers." << endl;
    } else {
        cout << num << " is not the multiplication of 3 prime numbers." << endl;
    }
    return 0