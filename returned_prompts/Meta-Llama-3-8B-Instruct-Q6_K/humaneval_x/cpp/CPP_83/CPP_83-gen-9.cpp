    int count = 0;
    // first digit is 1
    for (int i = 1; i <= 9; i++) {
        // second digit to nth digit
        for (int j = 1; j <= 9; j++) {
            for (int k = 0; k < n - 2; k++) {
                int num = i * 10 + j * 10^k + 1;
                count++;
            }
        }
    }
    // last digit is 1
    for (int i = 1; i <= 9; i++) {
        // second digit to nth digit
        for (int j = 0; j < n - 1; j++) {
            int num = i * 10^j + 1;
            count++;
        }
    }
    return count;
}

int main(){
    int n = 3;
    printf("%d\n", starts_one_ends(n));
    return 0;
}

B:
#include <iostream>
using namespace std;

int countNumbers(int n) {
    int count = 0;
    // numbers that start with 1
    for (int i = 1; i <= 9; i++) {
        // second digit to nth digit
        for (int j = 0; j < n - 1; j++) {
            // last digit can be anything
            for (int k = 0; k < 10; k++) {
                int num = i * 10^j + k + 1;
                count++;
            }
        }
    }
    // numbers that end with 1
    for (int i = 0; i < 10; i++) {
        // second digit to nth digit
        for (int j = 0; j < n - 1; j++) {
            // first digit can be anything
            for (int k = 0; k < 10; k++) {
                int num = k * 10^j + i;
                count++;
            }
        }
    }
    return count;
}

int main() {
    int n = 3;
    cout << countNumbers(n) << endl;
    return 0;
}

C:
#include <iostream>
using namespace std;

int countNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        for (