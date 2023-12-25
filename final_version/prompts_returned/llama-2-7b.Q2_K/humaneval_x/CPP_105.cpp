/*
Given a vector of integers, sort the integers that are between 1 and 9 inclusive,
reverse the resulting vector, and then replace each digit by its corresponding name from
"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

For example:
  arr = {2, 1, 1, 4, 5, 8, 2, 3}   
        -> sort arr -> {1, 1, 2, 2, 3, 4, 5, 8} 
        -> reverse arr -> {8, 5, 4, 3, 2, 2, 1, 1}
  return {"Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"}

  If the vector is empty, return an empty vector:
  arr = {}
  return {}

  If the vector has any strange number ignore it:
  arr = {1, -1 , 55} 
        -> sort arr -> {-1, 1, 55}
        -> reverse arr -> {55, 1, -1}
  return = {"One"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
vector<string> by_length(vector<int> arr){
	if(arr.size()==0)return vector<string>();//empty the array if empty
	sort(arr.begin(), arr.end());//sort the array so that they are in ascending order now we can reverse it
	reverse(arr.begin(), arr.end());//now we have to reverse them back again...so that the sorted digits remain the same and each digit is replaced by its name
	int i=0;int j,n,k;
	map<string,int> fp_map;//here we are creating a map with names as keys and their places in array(0-9) as values..so that when arr[i] has been replaced by its corresponding name from "One", "Two"...we can access it to replace that