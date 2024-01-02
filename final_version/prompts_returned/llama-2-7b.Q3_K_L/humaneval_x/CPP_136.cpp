/*
Create a function that returns a vector (a, b), where "a" is
the largest of negative integers, and "b" is the smallest
of positive integers in a vector.
If there is no negative or positive integers, return them as 0.

Examples:
largest_smallest_integers({2, 4, 1, 3, 5, 7}) == {0, 1}
largest_smallest_integers({}) == {0,0}
largest_smallest_integers({0}) == {0,0}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
	if(lst.size()==0) return 0;
	reverse(lst.begin(),lst.end());
	sort(lst);
	if(find(lst.rbegin(),lst.rend(),-1) != lst.rend())
	return to_vector(max(lst),min(lst));
	else{
	int n=0;
	for(auto& x:lst){
		n+=x;
	}
	return to_vector((int)n,0);
}
}
