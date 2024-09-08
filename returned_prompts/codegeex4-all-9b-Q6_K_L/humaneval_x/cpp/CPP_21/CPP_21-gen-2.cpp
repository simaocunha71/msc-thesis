#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

vector<float> rescale_to_unit(vector<float> numbers) {
    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    for (auto &num : numbers) {
        num = (num - min) / (max - min);
    }
    return numbers;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> rescaled = rescale_to_unit(numbers);
    for (const auto &num : rescaled) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
这个代码可以吗
