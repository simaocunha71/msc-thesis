/*
Create a function which returns the largest index of an element which
is not greater than or equal to the element immediately preceding it. If
no such element exists then return -1. The given vector will not contain
duplicate values.

Examples:
can_arrange({1,2,4,3,5}) = 3
can_arrange({1,2,3}) = -1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int can_arrange(vector<int> arr){
    int i = 0;
    while(i < arr.size() - 1){
        if(arr[i] > arr[i+1]){
            return i;
        }
        i++;
    }
    return -1;
}