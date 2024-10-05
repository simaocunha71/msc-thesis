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
	if(numbers.size()<2){
		printf("no numbers to compare\n");
		return vector<float>();
	}
	float min_diff=abs(numbers[1]-numbers[0]);
	int min_index=0;
	int max_index=1;
	for(int i=0;i<numbers.size();i++){
		if(i==0){
			continue;
		}
		if(abs(numbers[i]-numbers[i-1])<min_diff){
			min_diff=abs(numbers[i]-numbers[i-1]);
			min_index=i;
			max_index=i-1;
		}
	}
	vector<float> result;
	result.push_back(numbers[min_index]);
	result.push_back(numbers[max_index]);
	return result;
}
