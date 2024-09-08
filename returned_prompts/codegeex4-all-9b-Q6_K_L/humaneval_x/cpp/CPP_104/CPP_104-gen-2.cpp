#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> unique_digits(vector<int> x) {
    vector<int> result;
    for (auto i : x) {
        bool has_even_digit = false;
        while (i > 0) {
            int digit = i % 10;
            if (digit % 2 == 0) {
                has_even_digit = true;
                break;
            }
            i /= 10;
        }
        if (!has_even_digit) {
            result.push_back(i);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> input = {15, 33, 1422, 1};
    vector<int> output = unique_digits(input);
    for (auto i : output) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> unique_digits(vector<int> x) {
    vector<int> result;
    for (auto i : x) {
        bool has_even_digit = false;
        while (i > 0) {
            int digit = i % 10;
            if (digit % 2 == 0) {
                has_even_digit = true;
                break;
            }
            i /= 10;
        }
        if (!has_even_digit) {
            result.push_back(i);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> input = {15, 33, 1422, 1};
    vector<int> output = unique_digits(input);
    for (auto i : output) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
C:
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> unique_digits(vector<int> x) {
    vector<int> result;
    for (auto i : x) {
        bool has_even_digit = false;
        while (i > 0) {
            int digit = i % 10;
            if (digit % 2 == 0) {
                has_even_digit = true;
                break;
            }
            i /= 10;
        }
        if (!has_even_digit) {
            result.push_back(i);
        }
    }
    sort(result.begin