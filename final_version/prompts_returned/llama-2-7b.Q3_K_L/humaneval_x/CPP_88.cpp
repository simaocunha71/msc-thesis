/*
Given a vector of non-negative integers, return a copy of the given vector after sorting,
you will sort the given vector in ascending order if the sum( first index value, last index value) is odd,
or sort it in descending order if the sum( first index value, last index value) is even.

Note:
* don't change the given vector.

Examples:
* sort_vector({}) => {}
* sort_vector({5}) => {5}
* sort_vector({2, 4, 3, 0, 1, 5}) => {0, 1, 2, 3, 4, 5}
* sort_vector({2, 4, 3, 0, 1, 5, 6}) => {6, 5, 4, 3, 2, 1, 0}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> array){
	if(array.size()==0)return vector<int>();
	std::sort(array.begin(),array.end());
	int flag=1;
    for (int i = 0 ; i < array.size(); ++i ) {
        if((array[i] % 2) == 1 && flag==1)flag=0;
		else{
            if(array[i]%2!=1 || !flag) return vector<int>(array.begin(),array.end());
		}
    }
	return vector<int>(array.begin(),array.end());
}
int main(){
	vector<int> v={0,5};
	sort_array(v);
	for (int i = 0 ; i < v.size(); ++i ) {
        printf("%d ",v[i]);
    }
	return 0;
}