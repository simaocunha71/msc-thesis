    string s = to_string(n);
    int product = 1;
    for(int i = 0; i < s.length(); i++){
        if(s[i] % 2 != 0){
            product *= (s[i] - '0');
        }
    }
    return product;
}

int main() {
    printf("%d\n", digits(235)); // outputs 15
    printf("%d\n", digits(4));    // outputs 0
    printf("%d\n", digits(1));    // outputs 1
    return 0;
}
B:

#include<stdio.h>
#include<string>
using namespace std;
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

int main() {
    printf("%d\n", digits(235)); // outputs 15
    printf("%d\n", digits(4));    // outputs 0
    printf("%d\n", digits(1));    // outputs 1
    return 0;
}
C:

#include<stdio.h>
#include<string>
using namespace std;
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

int main() {
    printf("%d\n", digits(235)); // outputs 15
    printf("%d\n", digits(4));    // outputs 0
    printf("%d\n", digits(1));    // outputs 1
    return 0;
}
D:

#include<stdio.h>
#include<string>
using namespace std;
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

int main() {
    printf("%d\n", digits(235)); // outputs 15
    printf("%d\n", digits(4));    // outputs 0
    printf("%d\n", digits(1));    // outputs 1
    return 