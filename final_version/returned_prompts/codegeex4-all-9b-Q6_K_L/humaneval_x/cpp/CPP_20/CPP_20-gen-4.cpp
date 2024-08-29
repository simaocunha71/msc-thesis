#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <limits>
using namespace std;

pair<float, float> find_closest_elements(vector<float> numbers){
    if(numbers.size() < 2){
        throw invalid_argument("Input vector must have at least two elements");
    }

    sort(numbers.begin(), numbers.end());

    float min_diff = numeric_limits<float>::max();
    pair<float, float> closest_pair;

    for(int i = 0; i < numbers.size() - 1; i++){
        float diff = numbers[i+1] - numbers[i];
        if(diff < min_diff){
            min_diff = diff;
            closest_pair = {numbers[i], numbers[i+1]};
        }
    }

    return closest_pair;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    pair<float, float> closest_pair = find_closest_elements(numbers);
    cout << "(" << closest_pair.first << ", " << closest_pair.second << ")" << endl;

    numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.0};
    closest_pair = find_closest_elements(numbers);
    cout << "(" << closest_pair.first << ", " << closest_pair.second << ")" << endl;

    return 0;
}