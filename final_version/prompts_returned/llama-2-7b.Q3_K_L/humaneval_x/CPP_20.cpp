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
	int len = numbers.size();
	if (len < 2)return vector<int>();
	sort(numbers.begin(), numbers.end());
    float min, max=0.0f;
    for (int i=1; i<len-1; i++){
        float cur_max = numbers[i];
        
        if (max < cur_max) {
            max = cur_max;
            
            for (int j=i+1; j<len; j++){
                min = numbers[j] - 0.000000001f; // allow for rounding error
                if (min > cur_max) {
                    max = min;
                }
            }
        }
    }
	return vector<int>({number, (number-max)/(max+1)});
}