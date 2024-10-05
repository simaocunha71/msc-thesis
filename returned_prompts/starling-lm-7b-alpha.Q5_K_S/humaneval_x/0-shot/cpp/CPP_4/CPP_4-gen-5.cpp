    float mean = 0.0;
    for(int i = 0; i < numbers.size(); i++){
        mean += numbers[i];
    }
    mean /= numbers.size();

    float mad = 0.0;
    for(int i = 0; i < numbers.size(); i++){
        mad += fabs(numbers[i] - mean);
    }
    mad /= numbers.size();

    return mad;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("%.2f\n", mean_absolute_deviation(numbers));
    return 0;
}


























/*
For a given vector of input numbers, calculate Mean Absolute Deviation
around the mean of this dataset.
Mean Absolute Deviation is the average absolute difference between each
element and a centerpoint (mean in this case):
MAD = average | x - x_mean |
>>> mean_absolute_deviation({1.0, 2.0, 3.0, 4.0})
1.0
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float mean_absolute_deviation(vector<float> numbers){
    float mean = 0.0;
    for(int i = 0; i < numbers.size(); i++){
        mean += numbers[i];
    }
    mean /= numbers.size();

    float mad = 0.0;
    for(int i = 0; i < numbers.size(); i++){
        mad += fabs(numbers[i] - mean);
    }
    mad /= numbers.size();

    return mad;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0};
    printf("%.2f\n", mean_absolute_deviation(numbers));
    return 0;
}
