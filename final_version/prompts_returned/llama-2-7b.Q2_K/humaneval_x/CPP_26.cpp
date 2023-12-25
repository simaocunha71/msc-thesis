/*
From a vector of integers, remove all elements that occur more than once.
Keep order of elements left the same as in the input.
>>> remove_duplicates({1, 2, 3, 2, 4})
{1, 3, 4}
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> remove_duplicates(vector<int> numbers){
	vector<int> v;
	for (int i =0 ;i <numbers.size();i++) {
		v.push_back(numbers[i]);
	}
	sort(v.begin(), v.end());
	set<int> s;
	while(!s.empty())
	{
		for (int j = 0 ;j < numbers.size();j++) {
			if(s.count(numbers[i]))
			break;
		}
		printf("v[%d]=%d\n",j,v[j]);
		s.insert(numbers[i]);
	}
	return v;
}
int main(){
	vector<int> numbers = {1,2,3,4};
	remove_duplicates(numbers);
}

