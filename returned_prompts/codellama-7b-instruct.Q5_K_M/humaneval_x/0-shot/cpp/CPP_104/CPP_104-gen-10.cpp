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
    vector<int> y;
    for(int i=0;i<x.size();i++){
        if(x[i]%2!=0){
            y.push_back(x[i]);
        }
    }
    sort(y.begin(),y.end());
    return y;
}
int main(){
    vector<int> v;
    v.push_back(15);
    v.push_back(33);
    v.push_back(1422);
    v.push_back(1);
    vector<int> u = unique_digits(v);
    for(int i=0;i<u.size();i++){
        cout<<u[i]<<" ";
    }
    cout<<endl;
    return 0;
}
