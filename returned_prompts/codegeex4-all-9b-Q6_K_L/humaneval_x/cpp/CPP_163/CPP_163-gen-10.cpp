#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

vector<int> generate_integers(int a, int b) {
    vector<int> result;
    for (int i = a; i <= b; i++) {
        int num = i;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                result.push_back(digit);
            }
            num /= 10;
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> result = generate_integers(10, 14);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}

B:
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

vector<int> generate_integers(int a, int b) {
    vector<int> result;
    for (int i = a; i <= b; i++) {
        int num = i;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                result.push_back(digit);
            }
            num /= 10;
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> result = generate_integers(10, 14);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}

C:
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

vector<int> generate_integers(int a, int b) {
    vector<int> result;
    for (int i = a; i <= b; i++) {
        int num = i;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                result.push_back(digit);
            }
            num /= 10;
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> result = generate_integers(10, 14);
    for (int i = 0; i < result.size(); i++) {
        cout