#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int even = 0, odd = 0;
    while (n != 0) {
        int digit = n % 10;
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
        n = n / 10;
    }
    cout << "{" << even << ", " << odd << "}" << endl;
    return 0;
}
B:
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int even = 0, odd = 0;
    while (n != 0) {
        int digit = n % 10;
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
        n = n / 10;
    }
    cout << "[" << even << ", " << odd << "]" << endl;
    return 0;
}
C:
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int even = 0, odd = 0;
    while (n != 0) {
        int digit = n % 10;
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
        n = n / 10;
    }
    cout << "{" << even << ", " << odd << "}" << endl;
    return 0;
}
D:
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int even = 0, odd = 0;
    while (n != 0) {
        int digit = n % 10;
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
        }
        n = n / 10;
    }
    cout << "[" << even << ", " << odd << "]" << endl;
    return 0;
}
E:
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int even = 0, odd = 0;
    while (n != 0) {
        int digit = n % 10;
        if (digit % 2 == 0) {
            even++;
        } else {
            odd++;
       