    sort(l.begin(), l.end());
    vector<int> res;
    res.clear();
    int i;
    for(i = 0; i < l.size(); i++) {
        if(i == 0 || l[i] != l[i-1]) {
            res.push_back(l[i]);
        }
    }
    return res;
}

vector<int> unique(vector<int> l, int n) {
    if (n <= 0) return l;
    sort(l.begin(), l.end());
    vector<int> res;
    res.clear();
    int i;
    for(i = 0; i < l.size(); i++) {
        if(i == 0 || l[i] != l[i-1]) {
            res.push_back(l[i]);
        }
    }
    return res;
}

int main() {
    vector<int> v = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> u = unique(v);
    printf("{%d, %d, %d, %d, %d, %d, %d, %d, %d}\n", u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8]);
    return 0;
}


/*
Return sorted unique elements in a vector
>>> unique({5, 3, 5, 2, 3, 3, 9, 0, 123})
{0, 2, 3, 5, 9, 123}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> unique(vector<int> l){

    sort(l.begin(), l.end());
    vector<int> res;
    res.clear();
    int i;
    for(i = 0; i < l.size(); i++) {
        if