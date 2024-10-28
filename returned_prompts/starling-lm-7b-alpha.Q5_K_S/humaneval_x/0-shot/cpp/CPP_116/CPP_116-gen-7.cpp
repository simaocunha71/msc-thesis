
#include <bits/stdc++.h>
using namespace std;

vector<int> sort_vector(vector<int> v) {
    sort(v.begin(), v.end(), [](int a, int b) {
        int a_count = __builtin_popcount(a);
        int b_count = __builtin_popcount(b);
        if (a_count != b_count) {
            return a_count < b_count;
        } else {
            return a < b;
        }
    });
    return v;
}

int main() {
    vector<int> v = {1, 5, 2, 3, 4};
    for (int i : sort_vector(v)) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}


B:

#include <bits/stdc++.h>
using namespace std;

vector<int> sort_vector(vector<int> v) {
    sort(v.begin(), v.end(), [](int a, int b) {
        int a_count = __builtin_popcount(a);
        int b_count = __builtin_popcount(