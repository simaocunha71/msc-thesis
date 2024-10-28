    float max = -1, min = 1000000000;
    for(int i = 0; i < numbers.size(); i++) {
        max = max > numbers[i] ? max : numbers[i];
        min = min < numbers[i] ? min : numbers[i];
    }
    for(int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min)/(max - min);
    }
    return numbers;
}


Answer:
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
    float max = -1, min = 1000000000;
    for(int i = 0; i < numbers.size(); i++) {
        max = max > numbers[i] ? max : numbers[i];
        min = min < numbers[i] ? min : numbers[i];
    }
    for(int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min)/(max - min);
    }
    return numbers;
}




Explanation:
To solve this problem, we must find the maximum and minimum values in the vector and then apply a linear transform to each value in the vector such that the minimum value becomes 0 and the maximum value becomes 1. To do this, we can iterate through the vector and update the maximum and minimum values as we find them, and then apply the linear transform to each value in the vector by subtracting the minimum and dividing by the range