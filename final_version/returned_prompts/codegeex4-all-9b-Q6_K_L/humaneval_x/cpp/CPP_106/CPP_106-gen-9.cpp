#include <iostream>
#include <vector>

using namespace std;

vector<int> f(int n) {
    vector<int> out(n);
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            out[i] = 1;
            for (int j = 2; j <= i; ++j) {
                out[i] *= j;
            }
        } else {
            out[i] = i;
            for (int j = 1; j < i; ++j) {
                out[i] += j;
            }
        }
    }
    return out;
}

int main() {
    vector<int> result = f(5);
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
输出是1 2 3 4 5，不是1 2 6 24 15
B:
#include <iostream>
#include <vector>

using namespace std;

vector<int> f(int n) {
    vector<int> out(n);
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            out[i] = 1;
            for (int j = 2; j <= i; ++j) {
                out[i] *= j;
            }
        } else {
            out[i] = i;
            for (int j = 1; j < i; ++j) {
                out[i] += j;
            }
        }
    }
    return out;
}

int main() {
    vector<int> result = f(5);
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
输出是1 2 3 4 5，不是1 2 6 24 15
C:
#include <iostream>
#include <vector>

using namespace std;

vector<int> f(int n) {
    vector<int> out(n);
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            out[i] = 1;
            for (int j = 2; j <= i; ++j) {
               