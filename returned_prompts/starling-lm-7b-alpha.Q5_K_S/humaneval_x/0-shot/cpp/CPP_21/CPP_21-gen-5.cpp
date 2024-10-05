    float max = -1;
    float min = 100000;
    for (int i = 0; i < numbers.size(); i++) {
        if (max < numbers[i]) {
            max = numbers[i];
        }
        if (min > numbers[i]) {
            min = numbers[i];
        }
    }
    for (int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min) / (max - min);
    }
    return numbers;
}


/*
Given two vectors of numbers, find the smallest and largest difference between them
>>> find_differences({3.0, 4.0, 5.0}, {2.0, 4.0, 6.0})
(2.0, 4.0)
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> find_differences(vector<float> first, vector<float> second) {
    vector<float> result;
    if (first.size() != second.size()) {
        return result;
    }
    for (int i = 0; i < first.size(); i++) {
        float diff = first[i] - second[i];
        result.push_back(diff);
    }
    return result;
}


/*
Given a vector of numbers, find the median of the vector
If the vector has an even number of elements, return the mean of the two middle numbers
>>> median({1.0, 2.0, 3.0, 4.0})
2.0
>>> median({1.0, 2.0, 3.0, 4.0, 5.0})
2.5
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float median(vector<float> numbers) {
    if (numbers.size() % 2 == 0) {
        return (numbers[numbers.size() / 2]