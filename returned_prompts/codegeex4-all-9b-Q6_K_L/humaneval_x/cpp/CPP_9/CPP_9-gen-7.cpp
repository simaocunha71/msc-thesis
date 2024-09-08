#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

vector<int> rolling_max(vector<int> numbers) {
    vector<int> result;
    int current_max = INT_MIN;
    for (int i = 0; i < numbers.size(); i++) {
        current_max = max(current_max, numbers[i]);
        result.push_back(current_max);
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> rolling_max_result = rolling_max(numbers);
    for (int i = 0; i < rolling_max_result.size(); i++) {
        cout << rolling_max_result[i] << " ";
    }
    cout << endl;
    return 0;
}
