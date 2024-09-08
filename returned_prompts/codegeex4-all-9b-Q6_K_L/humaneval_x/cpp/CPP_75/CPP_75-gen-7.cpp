#include <iostream>
#include <cmath>
using namespace std;

bool is_multiply_prime(int a) {
    if(a < 2) return false;
    int count = 0;
    for(int i = 2; i <= a; i++) {
        if(a % i == 0) {
            bool is_prime = true;
            for(int j = 2; j <= sqrt(i); j++) {
                if(i % j == 0) {
                    is_prime = false;
                    break;
                }
            }
            if(is_prime) {
                count++;
                if(count > 3) return false;
            }
        }
    }
    return count == 3;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if(is_multiply_prime(num)) {
        cout << num << " is the multiplication of 3 prime numbers." << endl;
    } else {
        cout << num << " is not the multiplication of 3 prime numbers." << endl;
    }
    return 0;
}

B:
#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if(n <= 1) return false;
    for(int i = 2; i <= sqrt(n); i++) {
        if(n % i == 0) return false;
    }
    return true;
}

bool is_multiply_prime(int a) {
    if(a < 2) return false;
    int count = 0;
    for(int i = 2; i <= a; i++) {
        if(a % i == 0 && is_prime(i)) {
            count++;
            if(count > 3) return false;
        }
    }
    return count == 3;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if(is_multiply_prime(num)) {
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
    if(n <= 1) return false;
    for(int i = 2; i <= sqrt(n); i++) {
        if(n % i == 0) return false;
    }
    return true;
}

bool is