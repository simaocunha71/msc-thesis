```cpp
#include <vector>
#include <algorithm>
#include <numeric>

std::vector<float> rescale_to_unit(std::vector<float> numbers)
{
    float min_val = *std::min_element(numbers.begin(), numbers.end());
    float max_val = *std::max_element(numbers.begin(), numbers.end());
    float scale = 1.0 / (max_val - min_val);
    float shift = -min_val * scale;
    
    for (auto &num : numbers) {
        num = (num + shift) * scale;
    }
    
    return numbers;
}
```
This code first finds the minimum and maximum values in the input vector. It then calculates the scale factor and shift factor needed to transform the vector. The scale factor is the reciprocal of the difference between the maximum and minimum values, and the shift factor is the negative of the minimum value multiplied by the scale factor. The code then applies the transformation to each element in the vector, and returns the transformed vector.