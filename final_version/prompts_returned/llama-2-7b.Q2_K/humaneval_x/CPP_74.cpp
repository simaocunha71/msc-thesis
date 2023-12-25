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
	int size=0;
	for(auto x:lst1){
		size+=x.length();
	}
	for (auto x:lst2)
	{
		if(size>=x.length())break;
	}
	return lst1;
}
void print_v(vector<int> v){
	for(auto i=0;i<v.size();i++){
		printf("%d ",v[i]);
	}
	printf("\n");
}
int main(){
	int n,m,x;
	cin>>n>>m;
	vector<int> v1(n);
	for(auto i=0;i<n;i++){
		v1[i]=i+1;
	}
	vector<string> lst2={"hI", "hi", "hi", "hI", "1", "2", "3", "4", "5"};
	total_match(v1,lst2);
	print_v(v1);
}
