    vector<float> result;
    float min_diff = INFINITY;
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size()-1; i++){
        if (numbers[i+1] - numbers[i] < min_diff){
            min_diff = numbers[i+1] - numbers[i];
            result = {numbers[i], numbers[i+1]};
        }
    }
    return result;
}

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

vector<float> find_closest_elements(vector<float> numbers){

    vector<float> result;
    float min_diff = INFINITY;
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size()-1; i++){
        if (numbers[i+1] - numbers[i] < min_diff){
            min_diff = numbers[i+1] - numbers[i];
            result = {numbers[i], numbers[i+1]};
        }
    }
    return result;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> closest = find_closest_elements(numbers);
    cout << "(" << closest[0] << ", " << closest[1] << ")" << endl;
    return 0;
}

This code is written in C++ and it finds the two numbers in the supplied vector of numbers that are closest to each other. The function find_closest_elements takes a vector of floats as input and returns a vector of two floats. The numbers are sorted in ascending order, then the difference between each pair of successive numbers is calculated. If this difference is smaller than the current minimum difference, the pair of numbers is recorded and the minimum difference updated. Finally, the pair of numbers with the smallest difference is returned.

The main function tests this