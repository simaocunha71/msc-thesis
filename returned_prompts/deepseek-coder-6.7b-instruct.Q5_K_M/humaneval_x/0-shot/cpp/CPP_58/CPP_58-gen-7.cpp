#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> common(vector<int> l1, vector<int> l2){
    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());
    vector<int> commons;
    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(), back_inserter(commons));
    sort(commons.begin(), commons.end());
    commons.erase(unique(commons.begin(), commons.end()), commons.end());
    return commons;
}

int main() {
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> commons = common(l1, l2);
    for(int i=