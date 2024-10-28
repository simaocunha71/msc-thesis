	int min = INT_MAX, max = INT_MIN;
	for(int i = 0; i < numbers.size(); i++) {
		min = min < numbers[i] ? min : numbers[i];
		max = max > numbers[i] ? max : numbers[i];
	}
	
	for(int i = 0; i < numbers.size(); i++) {
		numbers[i] = (numbers[i] - min) / (max - min);
	}
	return numbers;
}


/*
Given a number, return a vector of numbers, such that the sum of all numbers in vector
equals to that number
>>> generate_numbers(3)
(1, 1, 1)
>>> generate_numbers(5)
(1, 1, 2, 1)
*/

#include<vector>
vector<int> generate_numbers(int sum) {
B:
	vector<int> result;
	for(int i = 1; i <= sum; i++) {
		result.push_back(i);
	}
	return result;
}

/*
Given two integers, find a vector of numbers (of at least two elements), such that:
- The sum of all numbers in vector equals to the first number
- The product of all numbers in vector equals to the second number
>>> find_numbers(2, 3)
(1, 3)
>>> find_numbers(6, 4)
(2, 3)
*/
vector<int> find_numbers(int sum, int product) {
C:
	for(int i = 1; i <= sqrt(product); i++) {
		if(product % i == 0) {
			int a = i, b = product / i;
			if(a + b == sum) {
				vector<int> result;
				result.push_back(a);
				result.push_back(b);
				return result;
			}
		}
	}
}


/*
Given a number