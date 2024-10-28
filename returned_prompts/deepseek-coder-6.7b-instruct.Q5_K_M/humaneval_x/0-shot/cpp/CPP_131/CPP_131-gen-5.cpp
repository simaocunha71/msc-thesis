    int res = 1, last_digit;
    while(n){
        last_digit = n % 10;
        if(last_digit % 2 != 0){
            res *= last_digit;
        }
        n /= 10;
    }
    return res == 1 ? 0 : res;
}



int main() {
    printf("%d\n", digits(1));
    printf("%d\n", digits(4));
    printf("%d\n", digits(235));
    return 0;
}

*/

// C++ Solution
#include <iostream>
using namespace std;

int digits(int n) {
    int res = 1, last_digit;
    while(n) {
        last_digit = n % 10;
        if(last_digit % 2 != 0){
            res *= last_digit;
        }
        n /= 10;
    }
    return res == 1 ? 0 : res;
}

int main() {
    cout << digits(1) << endl;
    cout << digits(4) << endl;
    cout << digits(235) << endl;
    return 0;
}

// C Solution
/*
#include <stdio.h>

int digits(int n) {
    int res = 1, last_digit;
    while(n) {
        last_digit = n % 10;
        if(last_digit % 2 != 0){
            res *= last_digit;
        }
        n /= 10;
    }
    return res == 1 ? 0 : res;
}

int main() {
    printf("%d\n", digits(1));
    printf("%d\n", digits(4));
    printf("%d\n", digits(235));
    return 0;
}
*/

/*
Test.assertEquals(digits(1), 1)
Test.assertEquals(digits(4), 0)
