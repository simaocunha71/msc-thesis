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
	vector<int> ans;
	for (int i=a+1 ;i<=b;i++){
	    if((i%2==0) && i>=a )
	        ans.push_back(i);
	}
	return ans;
}
