/*
From a given vector of integers, generate a vector of rolling maximum element found until given moment
in the sequence.
>>> rolling_max({1, 2, 3, 2, 3, 4, 2})
{1, 2, 3, 3, 3, 4, 4}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
	int curr = -1;
	int max_pos = INT_MIN;
	for (unsigned int i=0; i < numbers.size(); ++i) {
		if (curr == -1 || curr > numbers[i]) {
			curr = numbers[i];
			max_pos = i;
		}
	}
	int j = max_pos + 1;
	while(j <= max_pos){
		if (numbers[j] > curr) curr = numbers[j++];
		else break;
	}
	return curr;
}
void print(const vector<int> &v){
	for (auto i=0; i < v.size(); ++i) {
		printf("%d ", v[i]);
	}
	putchar('\n');
};
signed main(){
	print(rolling_max({1, 2, 3, 2, 3, 4, 2}));
	int a;
	scanf("%d", &a);
	printf("%d\n", rolling_max({-10,-9,-8,-7,-6}/*a is the vector to process*/));
}