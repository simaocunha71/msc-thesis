#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<float> rescale_to_unit(vector<float> numbers) {
    float min_val = *min_element(numbers.begin(), numbers.end());
    float max_val = *max_element(numbers.begin(), numbers.end());
    for (auto &num : numbers) {
        num = (num - min_val) / (max_val - min_val);
    }
    return numbers;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> result = rescale_to_unit(numbers);
    for (float num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
