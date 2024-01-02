/*
Given vector of integers, return vector in strange order.
Strange sorting, is when you start with the minimum value,
then maximum of the remaining integers, then minimum and so on.

Examples:
strange_sort_vector({1, 2, 3, 4}) == {1, 4, 2, 3}
strange_sort_vector({5, 5, 5, 5}) == {5, 5, 5, 5}
strange_sort_vector({}) == {}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> strange_sort_list(vector<int> lst){
	if(lst.size()==0) return {};
	std::sort (lst.begin(), lst.end());
	return lst; 
}
int main(){
   int test = 15;
   while(test--){
   		vector<int> lst = {1, 2, 3};
   		printf("%d: %s\n", test+1, strange_sort_list(lst).data());
   }
}
