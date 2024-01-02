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
	sort(numbers.begin(), numbers.end());
	int count = 0;
	vector<int> result;
	for (unsigned int i=0; i < numbers.size(); ++i) {
		if (count > 1 && numbers[i] == numbers[i-1]) {
			continue;
		}
		result.push_back(numbers[i]);
		++count;
	}
	return result;
}
int main() {
    int n = 5;
    vector<int> v1(n,rand());
    vector<int> v2(n, rand());
    cout<<remove_duplicates(v1)<<endl;
    cout<<remove_duplicates(v2)<<endl;
}
