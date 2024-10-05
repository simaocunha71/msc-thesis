/*
Given a vector of positive integers x. return a sorted vector of all 
elements that hasn't any even digit.

Note: Returned vector should be sorted in increasing order.

For example:
>>> unique_digits({15, 33, 1422, 1})
{1, 15, 33}
>>> unique_digits({152, 323, 1422, 10})
{}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> unique_digits(vector<int> x){

    vector<int> res;
    for (auto i : x) {
        if (i > 0) {
            if (i % 2 != 0) {
                res.push_back(i);
            }
        }
    }
    sort(res.begin(), res.end());
    return res;
}

