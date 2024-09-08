```cpp
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

pair<float, float> find_closest_elements(vector<float> numbers) {
    sort(numbers.begin(), numbers.end());
    float min_diff = INFINITY;
    pair<float, float> result;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < min_diff) {
            min_diff = diff;
            result = {numbers[i], numbers[i + 1]};
        }
    }

    return result;
}
```

The above function first sorts the vector of numbers. Then it iterates over the sorted vector, comparing the difference between adjacent elements. If the difference is smaller than the current minimum difference, it updates the minimum difference and the result. Finally, it returns the pair of numbers with the smallest difference.