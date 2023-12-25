/*
Write a function that accepts a vector of strings as a parameter,
deletes the strings that have odd lengths from it,
and returns the resulted vector with a sorted order,
The vector is always a vector of strings and never a vector of numbers,
and it may contain duplicates.
The order of the vector should be ascending by length of each word, and you
should return the vector sorted by that rule.
If two words have the same length, sort the vector alphabetically.
The function should return a vector of strings in sorted order.
You may assume that all words will have the same length.
For example:
assert vector_sort({"aa", "a", "aaa"}) => {"aa"}
assert vector_sort({"ab", "a", "aaa", "cd"}) => {"ab", "cd"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> sorted_list_sum(vector<string> lst){
	int i=0,j=0,k=1;  //iterate over each element of input vector
	for(i=0;i<=lst.size()-1;++i)//create a new vector that contains the sum of the elements in old vector
	{	vector<string> tmp_lst ;//create a temporary vector to store the sum of all the elements with even numbers in the input vector 
		while(i+k<=lst.size()-1){ //iterate over each element and add its even number 
			if(lst[i].length()%2==0)tmp_lst.push_back(lst[i]);//add it to the temporary vector
			++k;
		}
			while (j<lst.size()) { //iterate over each element and add its even number less than k
			if((j+k-1)<=lst.size()&&(lst[j+k-1]).length()%2==0){//test if the added odd element's length is even
			tmp_lst.push_back(lst[j]);}
			++j;}
			
		sorted_list=sort(