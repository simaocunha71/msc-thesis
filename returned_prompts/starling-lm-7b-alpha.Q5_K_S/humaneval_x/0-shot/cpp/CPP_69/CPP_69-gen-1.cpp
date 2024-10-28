#include <bits/stdc++.h>

using namespace std;

int search(vector<int> lst) {
    int freq = 0;
    int max = lst[0];
    while (freq < max) {
        int i;
        for (i = 0; i < lst.size(); ++i) {
            if (freq == lst[i]) {
                ++freq;
                goto A;
            }
        }
        return -1;
    }
    return max;
}

int main() {
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    cout << search(lst) << endl;
    return 0;
}


/*










*/































































































































































