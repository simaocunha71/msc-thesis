    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    for (vector<float>::iterator it = numbers.begin(); it != numbers.end(); ++it) {
        *it = (*it - min) / (max - min);
    }
    return numbers;
}





/*
Given vector of numbers (of at least two elements), apply a linear transform to that vector,
such that the smallest number will become 0 and the largest will become 1
>>> rescale_to_unit({1.0, 2.0, 3.0, 4.0, 5.0})
{0.0, 0.25, 0.5, 0.75, 1.0}
*/
#include<vector>
#include<algorithm>

std::vector<float> rescale_to_unit(std::vector<float> numbers){ 
    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    for (std::vector<float>::iterator it = numbers.begin(); it != numbers.end(); ++it) {
        *it = (*it - min) / (max - min);
    }
    return numbers;
}


































































/*
Given vector of numbers (of at least two elements), apply a linear transform to that vector,
such that the smallest number will become 0 and the largest will become 1
>>> rescale_to_unit({1.0, 2.0, 3.0, 4.0, 5.0})
{0.0, 0.25, 0.5, 0.75, 1.0}
*/
#include<stdio.h>
#include<math.h>
#include