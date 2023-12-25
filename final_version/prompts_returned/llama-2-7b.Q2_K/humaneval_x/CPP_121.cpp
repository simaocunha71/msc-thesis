/*
Given a non-empty vector of integers, return the sum of all of the odd elements that are in even positions.


Examples
solution({5, 8, 7, 1}) ==> 12
solution({3, 3, 3, 3, 3}) ==> 9
solution({30, 13, 24, 321}) ==>0
*/
#include<stdio.h>
#include<vector>
using namespace std;
int solutions(vector<int> lst){
	if(!lst.size()) return 0;
	else {
    	for (int i = 1; i < lst.size() + 1; ++i) { // odd positions
      		if(((i & 1) == 1) && ((i+1)&1 ) != 1){ // odd position
        		lst[i] += lst[i-2]; //sum even elements in the vector at the even positions
	    }
    	}
  	return (int)lst.back();
	}
}
