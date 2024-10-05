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

    vector<int> temp;
    vector<int> result;
    for(int i = 0; i < x.size(); i++){
        if(x[i] != 0){
            int j = 1;
            while(j <= x[i]){
                if(x[i] % j == 0){
                    temp.push_back(j);
                }
                j++;
            }
            if(temp.size() == 1){
                result.push_back(x[i]);
            }
            temp.clear();
        }
    }
    sort(result.begin(), result.end());
    return result;
}
int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> result = unique_digits(x);
    for(int i = 0; i < result.size(); i++){
        printf("%d\n", result[i]);
    }
    return 0;
}
