#include<bits/stdc++.h>
using namespace std;

int smallest_change(vector<int> arr) {
    int n = arr.size();
    int odd = 0;
    int even = 0;
    for (int i = 0; i < n; i++) {
        if (i == n / 2) {
            if (arr[i] != arr[i - 1])
                odd++;
            continue;
        }
        if (arr[i] != arr[n - 1 - i]) {
            if (i < n / 2)
                odd++;
            else
                even++;
        }
    }
    return min(odd, even);
}

int main() {
    vector<int> arr = {1, 2, 3, 5, 4, 7, 9, 6};
    cout << smallest_change(arr) << endl;
    return 0;
}




















































































