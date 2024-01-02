/*
Insert a number "delimeter" between every two consecutive elements of input vector `numbers"
>>> intersperse({}, 4)
{}
>>> intersperse({1, 2, 3}, 4)
{1, 4, 2, 4, 3}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> intersperse(vector<int> numbers, int delimeter){ 
	if(numbers.size() == 0) return vector<int>();

	for(int i = 0; i < numbers.size(); i++) {
		if(!(i % delimeter)) printf("%d",numbers[i]);
	}
	return numbers;
}