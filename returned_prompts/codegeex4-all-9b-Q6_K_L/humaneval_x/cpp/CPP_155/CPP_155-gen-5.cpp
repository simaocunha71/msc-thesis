#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> even_odd_count(int num) {
    vector<int> result;
    int even = 0;
    int odd = 0;

    if (num == 0) {
        even = 1;
    } else {
        while (num != 0) {
            int digit = abs(num % 10);
            if (digit % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            num /= 10;
        }
    }

    result.push_back(even);
    result.push_back(odd);
    return result;
}

int main() {
    vector<int> result = even_odd_count(123);
    cout << "Even: " << result[0] << ", Odd: " << result[1] << endl;
    return 0;
}

B:
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> even_odd_count(int num) {
    vector<int> result(2, 0);

    if (num == 0) {
        result[0] = 1;
        return result;
    }

    if (num < 0) {
        num = -num;
    }

    while (num > 0) {
        int digit = num % 10;
        if (digit % 2 == 0) {
            result[0]++;
        } else {
            result[1]++;
        }
        num /= 10;
    }

    return result;
}

int main() {
    vector<int> result = even_odd_count(123);
    cout << "Even: " << result[0] << ", Odd: " << result[1] << endl;
    return 0;
}

C:
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> even_odd_count(int num) {
    vector<int> result(2, 0);
    int even = 0;
    int odd = 0;

    if (num == 0) {
        even = 1;
    } else {
        while (num != 0) {
            int digit = abs(num % 10);
            if (digit % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            num /= 10;
        }
    }

    result[0] = even;
   