#include <iostream>
#include <vector>
using namespace std;

vector<int> tri(int n) {
    vector<int> vec;
    vec.push_back(3);
    vec.push_back(1);
    vec.push_back(2);

    if (n == 0) return vec;
    if (n == 1) return vec;
    if (n == 2) return vec;

    for (int i = 3; i <= n; i++) {
        vec.push_back(vec[i - 1] + vec[i - 2] + vec[i - 3]);
    }

    return vec;
}

int main() {
    vector<int> vec = tri(3);
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;

vector<int> tri(int n) {
    vector<int> vec;
    vec.push_back(3);
    vec.push_back(1);
    vec.push_back(2);

    if (n == 0) return vec;
    if (n == 1) return vec;
    if (n == 2) return vec;

    for (int i = 3; i <= n; i++) {
        if (i % 2 == 0) {
            vec.push_back(1 + i / 2);
        } else {
            vec.push_back(vec[i - 1] + vec[i - 2] + vec[i - 3]);
        }
    }

    return vec;
}

int main() {
    vector<int> vec = tri(3);
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    return 0;
}

C:
#include <iostream>
#include <vector>
using namespace std;

vector<int> tri(int n) {
    vector<int> vec;
    vec.push_back(3);
    vec.push_back(1);
    vec.push_back(2);

    if (n == 0) return vec;
    if (n == 1) return vec;
    if (n == 2) return vec;

    for (int i = 3; i <= n; i++) {
        if (i % 2 == 0) {
            vec.push_back(1 + i / 2);
        } else {
            vec.push_back