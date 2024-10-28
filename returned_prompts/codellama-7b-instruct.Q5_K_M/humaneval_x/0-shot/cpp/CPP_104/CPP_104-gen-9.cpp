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

    vector<int> result;

    for(int i=0; i<x.size(); i++){
        int temp = x[i];
        while(temp > 0){
            if(temp % 10 % 2 == 0){
                temp = temp / 10;
            }else{
                break;
            }
        }
        if(temp == 0){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main(){
    vector<int> v = {15, 33, 1422, 1};
    vector<int> result = unique_digits(v);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
