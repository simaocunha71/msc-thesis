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
	int counter = 0;
	for (int i = 1; i < numbers.size(); ++i)
	{
		//Checking if two elements of vector are closer to each other than given threshold or not
		if(fabs(numbers[i-1] - numbers[i]) <= fabs(threshold))counter++;
	}

	return counter == 0;
}
