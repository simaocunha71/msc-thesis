/*
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

For example:
generate_integers(2, 8) => {2, 4, 6, 8}
generate_integers(8, 2) => {2, 4, 6, 8}
generate_integers(10, 14) => {}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){
    int start = a;
    int end = b;
    vector<int> result;
    for(int i = start; i <= end; i++){
        int num = i;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                result.push_back(digit);
            }
            num = num / 10;
        }
    }
    return result;
}
