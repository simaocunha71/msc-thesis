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
	if(arr[0]==arr[1]){
		for(i=2; i<arr.size(); i++){
			if(arr[i]<=arr[i-1]){
				return -1;
			}
		}
	}else{
		int last_index=-1, prev_index=0;
		for(int i=1; i<arr.size(); i++){
			if((arr[i]>arr[prev_index])&&(arr[i-1]<=arr[last_index])){
				return -1;
			}else if(arr[i-1]==arr[last_index]){
				if((arr[i]>arr[prev_index])&&(arr[last_index+1]>=arr[last_index])){
					return -1;
				}
			}else if(!(arr[i-1]==arr[last_index])){
				prev_index=i-1;
				last_index=i;
			}
		}
	}
	if((last_index+1)==arr.size()) return -1;
	return last_index;
}