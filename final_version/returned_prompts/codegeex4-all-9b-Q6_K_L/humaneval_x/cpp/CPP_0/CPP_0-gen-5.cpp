#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    int i, j;
    for (i = 0; i < numbers.size(); i++) {
        for (j = i+1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    vector<float> numbers = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    float threshold = 0.3;
    bool result = has_close_elements(numbers, threshold);
    cout << (result ? "true" : "false") << endl;
    return 0;
}

