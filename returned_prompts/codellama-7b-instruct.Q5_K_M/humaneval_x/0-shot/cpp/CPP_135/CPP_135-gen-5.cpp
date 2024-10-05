/*
Create a function which returns the largest index of an element
which is not greater than or equal to the element immediately
preceding it. If no such element exists then return -1. The given
vector will not contain duplicate values.

Examples:
can_arrange({1,2,4,3,5}) = 3
can_arrange({1,2,3}) = -1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int can_arrange(vector<int> arr){

    int len = arr.size();
    if(len == 0){
        return -1;
    }
    if(len == 1){
        return -1;
    }
    if(len == 2){
        if(arr[0] <= arr[1]){
            return -1;
        }
        else{
            return 1;
        }
    }
    int prev = 0;
    for(int i = 1; i < len; i++){
        if(arr[i] > arr[i-1]){
            prev = i;
        }
    }
    return prev;
}

int main(){
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(4);
    v.push_back(3);
    v.push_back(5);
    int largest_index = can_arrange(v);
    printf("%d", largest_index);
    return 0;
}
