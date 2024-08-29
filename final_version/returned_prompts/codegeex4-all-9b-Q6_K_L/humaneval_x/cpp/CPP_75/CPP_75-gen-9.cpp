#include <iostream>
using namespace std;
#include <cmath>
bool is_multiply_prime(int num) {
    if (num < 2) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

bool is_multiply_of_three_primes(int num) {
    int count = 0;
    for (int i = 2; i <= num / 2; i++) {
        if (is_multiply_prime(i) && is_multiply_prime(num / i)) {
            count++;
            if (count == 3) return true;
        }
    }
    return false;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_of_three_primes(num)) {
        cout << num << " is a multiplication of three prime numbers." << endl;
    } else {
        cout << num << " is not a multiplication of three prime numbers." << endl;
    }
    return 0;
}

B:
#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

bool is_multiply_of_three_primes(int num) {
    int count = 0;
    for (int i = 2; i <= num / 2; i++) {
        if (is_prime(i) && is_prime(num / i)) {
            count++;
            if (count == 3) return true;
        }
    }
    return false;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_of_three_primes(num)) {
        cout << num << " is a multiplication of three prime numbers." << endl;
    } else {
        cout << num << " is not a multiplication of three prime numbers." << endl;
    }
    return 0;
}

C:

#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false