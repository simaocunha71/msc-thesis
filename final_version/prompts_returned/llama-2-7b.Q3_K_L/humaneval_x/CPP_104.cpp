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
	sort(x.begin(),x.end());
	vector<int> ans;
	for(unsigned int i=0;i<x.size();++i){
		if (x[i] % 2 == 0)continue;
		ans.push_back(x[i]);
	}
	return ans;
}
int main(){
	vector<int> v = {15,33,1422};
	unique_digits(v);
	return 0;
}