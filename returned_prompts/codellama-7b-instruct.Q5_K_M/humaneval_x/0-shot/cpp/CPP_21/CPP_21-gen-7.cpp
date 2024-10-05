/*
Given vector of numbers (of at least two elements), apply a linear transform to that vector,
such that the smallest number will become 0 and the largest will become 1
>>> rescale_to_unit({1.0, 2.0, 3.0, 4.0, 5.0})
{0.0, 0.25, 0.5, 0.75, 1.0}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> rescale_to_unit(vector<float> numbers){ 
    // TODO: your code here
    int max_index = 0;
    int min_index = 0;
    float min_value = 100000000.0;
    float max_value = -100000000.0;
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] > max_value) {
            max_index = i;
            max_value = numbers[i];
        }
        if (numbers[i] < min_value) {
            min_index = i;
            min_value = numbers[i];
        }
    }
    vector<float> res;
    for (int i = 0; i < numbers.size(); i++) {
        if (i == min_index) {
            res.push_back(0.0);
        }
        else if (i == max_index) {
            res.push_back(1.0);
        }
        else {
            res.push_back((numbers[i] - min_value) / (max_value - min_value));
        }
    }
    return res;
}
