	int cnt = 0,j;
	for(int i = 0;i < arr.size();i++){
		if(arr[i] == 0)continue;
		cnt++;
	}
	vector<int> cnts(cnt);
	for(int i = 0,j = 0;i < arr.size();i++){
		if(arr[i] == 0)continue;
		cnts[j++] = arr[i];
	}
	sort(cnts.begin(),cnts.end());
	vector<int> tmp = cnts;
	vector<int> res;
	for(int i = 0;i < arr.size();i++){
		if(arr[i] == 0)res.push_back(0);
		else res.push_back(tmp[i]);
	}
	return res;
}

B:
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
	sort(arr.begin(),arr.end(),[](int a,int b){
		return __builtin_popcount(a) < __builtin_popcount(b) || (__builtin_popcount(a) == __builtin_popcount(b) && a < b);
	});
	return arr;
}

*/

