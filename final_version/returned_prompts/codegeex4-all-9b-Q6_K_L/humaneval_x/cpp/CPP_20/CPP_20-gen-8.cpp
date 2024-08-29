```cpp
#include <vector>
#include <cmath>
#include <algorithm>
#include <limits>

using namespace std;

pair<float, float> find_closest_elements(vector<float> numbers) {
    if (numbers.size() < 2) {
        throw runtime_error("The vector must contain at least two elements");
    }

    pair<float, float> closest = make_pair(numbers[0], numbers[1]);
    float min_distance = fabs(numbers[0] - numbers[1]);

    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            float distance = fabs(numbers[i] - numbers[j]);
            if (distance < min_distance) {
                min_distance = distance;
                closest = make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j]));
            }
        }
    }

    return closest;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    pair<float, float> closest = find_closest_elements(numbers);
    printf("(%f, %f)\n", closest.first, closest.second); // Output: (2.0, 2.2)

    numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.0};
    closest = find_closest_elements(numbers);
    printf("(%f, %f)\n", closest.first, closest.second); // Output: (2.0, 2.0)

    return 0;
}
```

这个C++代码实现了从给定的数字向量中选择并返回两个最接近的数字，并按顺序返回它们（较小的数字，较大的数字）。代码首先检查输入向量是否至少包含两个元素，然后使用嵌套循环计算每对数字之间的距离，并更新最小距离和最接近的数字对。最后，返回最接近的数字对。