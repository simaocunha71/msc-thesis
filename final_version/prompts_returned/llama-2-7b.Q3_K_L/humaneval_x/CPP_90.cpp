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
	if(lst.size()==0) return -1;
	int min=(*std::min_element)(lst.begin(),lst.end());  //finding the lowest element
	for(auto i=lst.begin();i!=lst.end();++i){
		if(*i<min) min = *i;
	}
return (int)min ;
}
int main(){
	vector<int> lst={1, 2, 3, 4, 5};
	next_smallest(lst);
	system("pause");
	return 0;
}