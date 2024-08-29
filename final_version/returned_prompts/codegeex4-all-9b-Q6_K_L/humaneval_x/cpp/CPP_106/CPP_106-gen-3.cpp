#include <iostream>
#include <vector>
using namespace std;

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int sum(int n) {
    return n * (n + 1) / 2;
}

vector<int> f(int n) {
    vector<int> result(n);
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            result[i] = factorial(i + 1);
        } else {
            result[i] = sum(i + 1);
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<int> result = f(n);
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int sum(int n) {
    return n * (n + 1) / 2;
}

vector<int> f(int n) {
    vector<int> result(n);
    for (int i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            result[i] = factorial(i);
        } else {
            result[i] = sum(i);
        }
    }
    return result;
}

int main() {
    int n = 5;
    vector<int> result = f(n);
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
using namespace std;

long long factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int sum(int n) {
    return n * (n + 1) / 2;
}

vector<int> f(int n) {
    vector<int> result(n);
    for (int i = 1; i <= n; ++i) {
        if (i % 2 == 0) {
            result[i