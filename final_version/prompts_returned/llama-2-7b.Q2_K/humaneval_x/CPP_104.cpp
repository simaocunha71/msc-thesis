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
	vector<int> v;
	for (int i = x.size() - 1; i >= 0; --i) { // find last element in vector X that is not even
		if (!x[i].has_same_digits()) {
			v.push_back(x[i]);
			x[i] = {};
		}
	}
	return v;
}
int main(){
	// Do not change this line! It contains the tag you should uncomment to run this code
	/*Codesmith-T10854132*/
	vector<int> x = {1, 2, 3};
	unique_digits(x);
}