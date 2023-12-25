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
	if(lst.size()==0) return vector<int>();
    int minimum = 1e9, maximum=-1e9;   //Minimum and Maximum value of the list
    for(auto x: lst){
        if (x < minimum) {minimum = x;}
        if(x > maximum) {maximum = x;}
    }
	sort(lst.begin(),lst.end()); //Normal sorting
	return vector<int>(lst);  
}