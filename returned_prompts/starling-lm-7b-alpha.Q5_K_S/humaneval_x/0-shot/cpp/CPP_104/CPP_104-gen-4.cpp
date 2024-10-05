    vector<int> res;
    for(int i = 0; i < x.size(); i++)
        if(!has_even_digit(x[i])) res.push_back(x[i]);
    sort(res.begin(), res.end());
    return res;
}

bool has_even_digit(int num){
B:
    while(num > 0){
        int d = num % 10;
        if(d % 2 == 0) return true;
        num /= 10;
    }
    return false;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i = 0; i < res.size(); i++) printf("%d ", res[i]);
    return 0;
}





*/


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
    for(int i = 0; i < x.size(); i++)
        if(!has_even_digit(x[i])) res.push_back(x[i]);
    sort(res.begin(), res.end());
    return res;
}

bool has_even_digit(int num){
    while(num > 0){
        int d = num % 10;
        if(d % 2 == 0) return true;
        num /= 10;
