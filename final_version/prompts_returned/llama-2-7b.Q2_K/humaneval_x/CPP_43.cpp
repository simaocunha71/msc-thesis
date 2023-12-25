/*
pairs_sum_to_zero takes a vector of integers as an input.
it returns true if there are two distinct elements in the vector that
sum to zero, and false otherwise.
>>> pairs_sum_to_zero({1, 3, 5, 0})
false
>>> pairs_sum_to_zero({1, 3, -2, 1})
false
>>> pairs_sum_to_zero({1, 2, 3, 7})
false
>>> pairs_sum_to_zero({2, 4, -5, 3, 5, 7})
true
>>> pairs_sum_to_zero({1})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool pairs_sum_to_zero(vector<int> l){
	if(l.size()==0)return false;
	else return (a[l.size()-1]-(a[0])>=(l[l.size()-2]-(l[0])));
}
int main(){
	vector<int> a={0, 1, 3, -2};
	printf("%d\n", pairs_sum_to_zero(a));
	return 0;
}