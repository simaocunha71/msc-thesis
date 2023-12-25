/*
From a supplied vector of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).
>>> find_closest_elements({1.0, 2.0, 3.0, 4.0, 5.0, 2.2})
(2.0, 2.2)
>>> find_closest_elements({1.0, 2.0, 3.0, 4.0, 5.0, 2.0})
(2.0, 2.0)
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> find_closest_elements(vector<float> numbers){
	int size = numbers.size();
	if (size < 3) throw "ERROR: vector is too small, must be at least three\n";
	else if (numbers[0] == numbers[1]) throw "ERROR: Two elements are the same.\n";
	float first_number_value = numbers[0], last_number_value = numbers.back();
	int min_distance = 99;
	float minimum = first_number_value, maximum = last_number_value;
	// Check to see if the elements are close enough, if so we can just return them already sorted and
	// not have to do the calculation.
	for (int i = 1; i < size - 1; ++i) {
		if ((numbers[0] == numbers[2*i]) && (min_distance > abs(first_number_value, last_number_value))) { // if we already have two equal elements then return them
			if (minimum >= first_number_value) minimum = first_number_value;
			return vector<float>{ numbers[0], numbers[2*i]};
		}
	}
	// If that failed, we have to work out the closest two elements and then sort them.
	min_distance = sqrt(pow((maximum - minimum), 2) + pow(99 - minimum, 2));
	int min; // The