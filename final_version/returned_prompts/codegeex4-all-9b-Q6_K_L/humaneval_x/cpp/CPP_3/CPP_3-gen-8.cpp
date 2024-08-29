/*
You"re given a vector of deposit and withdrawal operations on a bank account that starts with
zero balance. Your task is to detect if at any point the balance of account falls below zero, and
at that point function should return true. Otherwise it should return false.
>>> below_zero({1, 2, 3})
false
>>> below_zero({1, 2, -4, 5})
true
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool below_zero(vector<int> operations){
    int sum = 0;
    for(int i = 0; i < operations.size(); i++){
        sum += operations[i];
        if(sum < 0){
            return true;
        }
    }
    return false;
}