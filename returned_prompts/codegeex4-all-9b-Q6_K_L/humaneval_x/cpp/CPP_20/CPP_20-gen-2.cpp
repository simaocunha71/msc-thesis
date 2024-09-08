```cpp
#include <algorithm>
#include <vector>
using namespace std;

pair<float, float> find_closest_elements(const vector<float>& numbers) {
    if (numbers.size() < 2) return {0, 0};

    sort(numbers.begin(), numbers.end());
    float min_diff = abs(numbers[1] - numbers[0]);
    pair<float, float> min_pair = {numbers[0], numbers[1]};
    for (size_t i = 1; i < numbers.size() - 1; ++i) {
        float diff = abs(numbers[i+1] - numbers[i]);
        if (diff < min_diff) {
            min_diff = diff;
            min_pair = {numbers[i], numbers[i+1]};
        }
    }
    return min_pair;
}
```