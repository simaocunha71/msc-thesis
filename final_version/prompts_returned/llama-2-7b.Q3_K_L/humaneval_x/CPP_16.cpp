/*
Given a string, find out how many distinct characters (regardless of case) does it consist of
>>> count_distinct_characters("xyzXYZ")
3
>>> count_distinct_characters("Jerry")
4
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int count_distinct_characters(string str){ 
	if(str.length()==0) return 0; //empty
	//sort the string and store elements in vector of int values
	sort(str.begin(), str.end());
	vector<int> v;
	for(int i=0;i<str.length();++i){
		if(!v.count((unsigned)str[i]))//add the element to the vector if it is not present yet
			v.push_back((unsigned)str[i]);
	}
	return v.size();
} 