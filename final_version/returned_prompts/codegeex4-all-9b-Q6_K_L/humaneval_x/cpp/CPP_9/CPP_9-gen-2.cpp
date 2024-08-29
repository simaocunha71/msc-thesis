def rolling_max(numbers):
    maxes = []
    current_max = float('-inf')
    for n in numbers:
        if n > current_max:
            current_max = n
        maxes.append(current_max)
    return maxes

C:
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> rolling_max(vector<int> numbers) {
    vector<int> maxes;
    int current_max = INT_MIN;
    for (int n : numbers) {
        if (n > current_max) {
            current_max = n;
        }
        maxes.push_back(current_max);
    }
    return maxes;
}

