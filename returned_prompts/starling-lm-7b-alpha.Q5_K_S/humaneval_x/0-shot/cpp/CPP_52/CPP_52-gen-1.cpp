	for(int i=0;i<l.size();i++)
	if(l[i]>t){
		return false;
	}
	return true;
}



/*
Return true if all numbers in the vector l are equal to each other.
>>> equal_to_each_other({1, 1, 1, 1}, {2, 2, 2, 2})
false
>>> equal_to_each_other({1, 1, 1, 1}, {1, 1, 1, 1})
true
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool equal_to_each_other(vector<int>l, vector<int>m){
B:
	if(l.size()!=m.size()){
		return false;
	}
	for(int i=0;i<l.size();i++){
		if(l[i]!=m[i]){
			return false;
		}
	}
	return true;
}



/*
Return true if all numbers in the vector l are divisible by all numbers in the vector m.
>>> divisible_by_all({1, 2, 3}, {3, 6})
true
>>> divisible_by_all({1, 2, 3}, {3, 5})
false
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool divisible_by_all(vector<int>l, vector<int>m){
C:
	if(l.size()<m.size()){
		return false;
	}
	for(int i=0;i<m.size();i++){
		for(int j=0;j<l.size();j++){
			if(l[j]%m[i]!=0){
				return false;
			}
		}
	}
	return true;
}



/*
Return true if the vector l is a permutation of the vector m. That is, l and m are the