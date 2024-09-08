#include <cmath>
#include <vector>

std::vector<float> rescale_to_unit(const std::vector<float>& numbers) {
    float min = numbers[0];
    float max = numbers[0];
    for (float number : numbers) {
        if (number < min) {
            min = number;
        }
        if (number > max) {
            max = number;
        }
    }
    std::vector<float> rescaled_numbers;
    for (float number : numbers) {
        float rescaled_number = (number - min) / (max - min);
        rescaled_numbers.push_back(rescaled_number);
    }
    return rescaled_numbers;
}
