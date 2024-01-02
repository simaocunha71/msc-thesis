/*
Write a function that accepts two vectors of strings and returns the vector that has 
total number of chars in the all strings of the vector less than the other vector.

if the two vectors have the same number of chars, return the first vector.

Examples
total_match({}, {}) ➞ {}
total_match({"hi", "admin"}, {"hI", "Hi"}) ➞ {"hI", "Hi"}
total_match({"hi", "admin"}, {"hi", "hi", "admin", "project"}) ➞ {"hi", "admin"}
total_match({"hi", "admin"}, {"hI", "hi", "hi"}) ➞ {"hI", "hi", "hi"}
total_match({"4"}, {"1", "2", "3", "4", "5"}) ➞ {"4"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> total_match(vector<string> lst1,vector<string> lst2){
	int l=lst1.size();
	if(l==lst2.size()||l!=0)
	{
		for(unsigned int i = 0;i<lst1.size();++i)
		{
			if(lst1[i].length()>=lst2[i].length())
			return lst1;
			else
				return lst2;
		}
	}
	else return lst1;
}

int main(){
    vector<string> v1={"hi", "admin"};
    	vector<string> v2={"hI", "Hi"};
    	v1=total_match(v1,v2);
    	for (auto x:v1)
    	{
        	printf("%s ",x.c_str());
    	}
    return 0;
}