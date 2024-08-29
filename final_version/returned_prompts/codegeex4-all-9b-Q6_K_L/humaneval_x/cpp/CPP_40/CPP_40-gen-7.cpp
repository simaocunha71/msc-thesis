/*
triples_sum_to_zero takes a vector of integers as an input.
it returns true if there are three distinct elements in the vector that
sum to zero, and false otherwise.

>>> triples_sum_to_zero({1, 3, 5, 0})
false
>>> triples_sum_to_zero({1, 3, -2, 1})
true
>>> triples_sum_to_zero({1, 2, 3, 7})
false
>>> triples_sum_to_zero({2, 4, -5, 3, 9, 7})
true
>>> triples_sum_to_zero({1})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool triples_sum_to_zero(vector<int> l){
    sort(l.begin(), l.end());
    for(int i=0;i<l.size();i++){
        int j=i+1;
        int k=l.size()-1;
        while(j<k){
            int sum = l[i]+l[j]+l[k];
            if(sum==0){
                return true;
            }
            else if(sum<0){
                j++;
            }
            else{
                k--;
            }
        }
    }
    return false;
}