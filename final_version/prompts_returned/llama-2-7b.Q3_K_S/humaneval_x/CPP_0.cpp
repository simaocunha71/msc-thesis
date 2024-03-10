/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements({1.0, 2.0, 3.0}, 0.5)
false
>>> has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
true
*/
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
	int size=numbers.size();
	for (int i = 0;i < size-1;++i) { //iterate over all element in the vector except last element
		if (abs(fabs(numbers[i]) - fabs(numbers[i+1]))<threshold){//check whether distance between two numbers are less than given threshold
			return true;
		}
		else return false; //return false if any number in vector is not in pair with another number
	}
	int last=size-1;
	float diff = abs(fabs(numbers[last]) - fabs(numbers[last+1])) < threshold ? 0 : 1;//if distance between two numbers are less than given threshold then diff is zero , else dif is one
	return diff==0; //return true if diff (distance between two numbers) is less than given threshold else return false
}