    bool found = false;
    for(int i = 0; i < l.size(); i++) {
        for(int j = i + 1; j < l.size(); j++) {
            if(l[i] + l[j] == 0) {
                found = true;
                break;
            }
        }
        if(found) {
            break;
        }
    }
    return found;
}
int main() {
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 5, 7};
    vector<int> v5 = {1};
    cout << "v1: " << (pairs_sum_to_zero(v1) ? "true" : "false") << endl;
    cout << "v2: " << (pairs_sum_to_zero(v2) ? "true" : "false") << endl;
    cout << "v3: " << (pairs_sum_to_zero(v3) ? "true" : "false") << endl;
    cout << "v4: " << (pairs_sum_to_zero(v4) ? "true" : "false") << endl;
    cout << "v5: " << (pairs_sum_to_zero(v5) ? "true" : "false") << endl;
    return 0;
}
// Answer
#include<stdio.h>
#include<vector>
using namespace std;
bool pairs_sum_to_zero(vector<int> l){
    bool found = false;
    sort(l.begin(), l.end());
    for(int i = 0; i < l.size(); i++) {
        int j = i + 1;
        while(j < l.size() && l[j] <= -l[i]) {
            if(l[i] + l[j] == 0) {
                found = true;
                break;
            }
            j++;
        }
        if(found) {
            break;
        }
    }
    return found;
}
int main() {
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
