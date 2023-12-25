/*
You are given a vector of integers.
Write a function next_smallest() that returns the 2nd smallest element of the vector.
Return None if there is no such element.

next_smallest({1, 2, 3, 4, 5}) == 2
next_smallest({5, 1, 4, 3, 2}) == 2
next_smallest({}) == None
next_smallest({1, 1}) == None
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int next_smallest(vector<int> lst){
	if(lst.size()==0) return -1; // if v is empty, return -1

	sort(lst.begin(), lst.end());

	int i = 0;
	while (i < lst.size()) {
		if(lst[i]>lst[i+1]) { // the second element cannot be greater than first element
			return lst[i];
		} else {
			i++;
		}
	}
	return -1;

}
int main(){
	vector<int> v = {0, 1, 2, 3, 4};
	next_smallest(v);

	return 0;
}
