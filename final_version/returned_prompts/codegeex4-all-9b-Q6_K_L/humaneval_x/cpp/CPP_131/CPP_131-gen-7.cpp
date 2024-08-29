#include <iostream>
using namespace std;

int digits(int n) {
    int product = 1;
    while(n != 0) {
        int digit = n % 10;
        if(digit % 2 != 0)
            product *= digit;
        n /= 10;
    }
    return product;
}

int main() {
    int n = 235;
    cout << "Product of odd digits of " << n << " is " << digits(n) << endl;
    return 0;
}
B:
#include <iostream>
using namespace std;

int digits(int n) {
    int product = 1;
    while(n != 0) {
        int digit = n % 10;
        if(digit % 2 != 0)
            product *= digit;
        n /= 10;
    }
    return product;
}

int main() {
    int n = 235;
    cout << "Product of odd digits of " << n << " is " << digits(n) << endl;
    return 0;
}

C:
#include <iostream>
using namespace std;

int digits(int n) {
    int product = 1;
    while(n != 0) {
        int digit = n % 10;
        if(digit % 2 != 0)
            product *= digit;
        n /= 10;
    }
    return product;
}

int main() {
    int n = 235;
    cout << "Product of odd digits of " << n << " is " << digits(n) << endl;
    return 0;
}

D:
#include <iostream>
using namespace std;

int digits(int n) {
    int product = 1;
    while(n != 0) {
        int digit = n % 10;
        if(digit % 2 != 0)
            product *= digit;
        n /= 10;
    }
    return product;
}

int main() {
    int n = 235;
    cout << "Product of odd digits of " << n << " is " << digits(n) << endl;
    return 0;
}

E:
#include <iostream>
using namespace std;

int digits(int n) {
    int product = 1;
    while(n != 0) {
        int digit = n % 10;
        if(digit % 2 != 0)
            product *= digit;
        n /= 10;
    }
    return product;
}

int main() {
    int n = 