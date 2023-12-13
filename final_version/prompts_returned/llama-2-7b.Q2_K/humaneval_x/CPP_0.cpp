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
	for (size_t i=1;i<numbers.size();++i) if (fabs(numbers[0] - numbers[i]) < 0.5) ++counter;
	if (counter > 0 && counter < numbers.size() / 2 ) return true ; else return false;
}