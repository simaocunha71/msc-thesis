/*
For a given vector of integers, return a vector consisting of a sum and a product of all the integers in a vector.
Empty sum should be equal to 0 and empty product should be equal to 1.
>>> sum_product({})
(0, 1)
>>> sum_product({1, 2, 3, 4})
(10, 24)
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> sum_product(vector<int> numbers){
	if(numbers.size() == 0){
		return {0,1};
	}
	else{
		sort(numbers.begin(), numbers.end());

		for(int i = 0; i < numbers.size(); ++i)
			cout << numbers[i] << " ";
		cout << endl;

		return {sumOfAllNumbers(numbers), productOfAllNumbers(numbers)};
	}
}
int sum_of_all_numbers(vector<int> v){
	int a = 0;
	for(int i = 0; i < v.size(); ++i)
		a += v[i];
	return a;
}

int productOfAllNumbers(vector<int> v){
	int b = 1;
	for(int i = 0; i < v.size(); ++i)
		b *= v[i];
	return b;
}