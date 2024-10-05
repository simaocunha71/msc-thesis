/*
In this Kata, you have to sort a vector of non-negative integers according to
number of ones in their binary representation in ascending order.
For similar number of ones, sort based on decimal value.

It must be implemented like this:
>>> sort_vector({1, 5, 2, 3, 4}) == {1, 2, 3, 4, 5}
>>> sort_vector({-2, -3, -4, -5, -6}) == {-6, -5, -4, -3, -2}
>>> sort_vector({1, 0, 2, 3, 4}) == {0, 1, 2, 3, 4}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> arr){
	vector<int> arr1;
	for(int i=0;i<arr.size();i++){
		int count=0;
		while(arr[i]>0){
			count++;
			arr[i]=(arr[i]-1)%10;
			arr[i]/=10;
		}
		arr1.push_back(count);
	}
	for(int i=0;i<arr1.size();i++){
		for(int j=i+1;j<arr1.size();j++){
			if(arr1[i]<arr1[j]){
				swap(arr1[i],arr1[j]);
			}
		}
	}
	vector<int> arr2;
	for(int i=0;i<arr1.size();i++){
		for(int j=0;j<arr.size();j++){
			if(arr1[i]==0){
				arr2.push_back(j);
			}
		}
	}
	for(int i=0;i<arr2.size();i++){
		