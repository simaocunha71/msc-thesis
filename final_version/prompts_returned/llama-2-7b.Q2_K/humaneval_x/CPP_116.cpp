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
	sort(arr.begin(),arr.end());
	for (int i = 0 ; i<arr.size();i++){
		cout<<arr[i]<< " ";
	}
	return arr;
}
void sort_inverse(vector<int> &v){
	sort_array(v);
}
struct greater
{
	bool operator () (const int& a, const int& b) const
	{
		return abs(a-b)>=abs(b-a);
	}
};
void sort_inverse(vector<int> &v){
	sort_array(v);
	reverse(v.begin(), v.end());
}
struct greater1
{
	bool operator () (const int& a, const int& b) const
	{
		return abs(a-b)>=abs(b-a);
	}
};
void sort_inverse(vector<int> &v){
	sort_array(v);
	reverse(v.begin(), v.end());
	for (unsigned int i = 0 ; i < v.size();i++){
		if ((abs((int)i-1)<abs((int)(v[v.size()-1])))||(abs((int)