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
    float min_diff = 1000;
    float a, b;
    for(int i = 0; i < numbers.size(); i++){
        for(int j = i+1; j < numbers.size(); j++){
            if(abs(numbers[i] - numbers[j]) < min_diff){
                min_diff = abs(numbers[i] - numbers[j]);
                a = numbers[i];
                b = numbers[j];
            }
        }
    }
    vector<float> result;
    result.push_back(a);
    result.push_back(b);
    return result;
}