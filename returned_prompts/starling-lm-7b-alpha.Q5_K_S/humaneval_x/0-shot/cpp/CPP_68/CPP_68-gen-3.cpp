
#include <bits/stdc++.h>

using namespace std;

vector<int> pluck(vector<int> arr) {
    if (arr.size() == 0) return {};
    int mn = 1000000000, idx = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0) {
            if (mn > arr[i]) {
                mn = arr[i];
                idx = i;
            }
        }
    }
    return {mn, idx};
}

int main() {
    vector<int> arr = {1, 2, 3};
    vector<int> ans = pluck(arr);
    cout << "{ " << ans[0] << ", " << ans[1] << " }" << endl;
    return 0;
}


































































































