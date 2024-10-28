
#include <bits/stdc++.h>
using namespace std;

vector<int> even_odd_palindrome(int n) {
    vector<int> res(2);
    for (int i = 1; i <= n; i++) {
        string s = to_string(i);
        if (s == string(s.rbegin(), s.rend())) {
            if (i % 2 == 0)
                res[0]++;
            else
                res[1]++;
        }
    }
    return res;
}

int main() {
    int n;
    cin >> n;
    vector<int> res = even_odd_palindrome(n);
    cout << res[0] << ' ' << res[1];
    return 0;
}

































































































































































