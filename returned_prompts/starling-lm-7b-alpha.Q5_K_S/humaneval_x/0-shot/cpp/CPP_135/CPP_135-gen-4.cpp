
#include <bits/stdc++.h>
using namespace std;

int can_arrange(vector<int> arr) {
    int n = arr.size();
    int max = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
            for (int j = i - 1; j >= 0; j--) {
                if (arr[j] >= max) {
                    continue;
                } else {
                    max = arr[i];
                    break;
                }
            }
        }
    }
    return max;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << can_arrange(arr);
    return 0;
}
































































































