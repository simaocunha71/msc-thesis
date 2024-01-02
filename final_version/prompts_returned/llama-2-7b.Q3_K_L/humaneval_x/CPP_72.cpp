/*
Write a function that returns true if the object q will fly, and false otherwise.
The object q will fly if it's balanced (it is a palindromic vector) and the sum of its elements is less than or equal the maximum possible weight w.

Example:
will_it_fly({1, 2}, 5) ➞ false 
// 1+2 is less than the maximum possible weight, but it's unbalanced.

will_it_fly({3, 2, 3}, 1) ➞ false
// it's balanced, but 3+2+3 is more than the maximum possible weight.

will_it_fly({3, 2, 3}, 9) ➞ true
// 3+2+3 is less than the maximum possible weight, and it's balanced.

will_it_fly({3}, 5) ➞ true
// 3 is less than the maximum possible weight, and it's balanced.
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
	if(q.size()==0) return true;
	//checks if the vector is a palindrome:
	int i,j;
	for (i = 0; i < q.size(); ++i) {
	    for (j = q.size() - 1; j >= 0; --j)
	        if(q[j] != q[i]) return false;
	}
	int sum=0;
	for(i=0;i<q.size();i++){
	    sum+=(i+1)*q[i];
	}
	if(sum<=w)return true;
	else return false;
}
