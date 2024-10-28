
#include <bits/stdc++.h>
using namespace std;

int search(vector<int> lst) {
    int max = -1;
    for (int i = 0; i < lst.size(); i++) {
        int cnt = 0;
        for (int j = 0; j < lst.size(); j++) {
            if (lst[i] == lst[j]) cnt++;
        }
        if (cnt >= lst[i] && max < lst[i]) max = lst[i];
    }
    return max == -1 ? -1 : max;
}

int main() {
    vector<int> lst;
    lst.push_back(4);
    lst.push_back(1);
    lst.push_back(2);
    lst.push_back(2);
    lst.push_back(3);
    lst.push_back(1);
    cout << search(lst) << endl;
    return 0;
}







































