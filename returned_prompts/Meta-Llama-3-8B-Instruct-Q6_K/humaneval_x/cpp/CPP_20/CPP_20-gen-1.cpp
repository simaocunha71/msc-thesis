    float min_diff = numeric_limits<float>::max();
    float closest_pair[2];
    for (int i = 0; i < numbers.size() - 1; i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            float diff = abs(numbers[i] - numbers[j]);
            if (diff < min_diff) {
                min_diff = diff;
                closest_pair[0] = numbers[i];
                closest_pair[1] = numbers[j];
            }
        }
    }
    return vector<float>(closest_pair, closest_pair+2);
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    for (float num : result) {
        printf("%f ", num);
    }
    printf("\n");
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

std::vector<float> find_closest_elements(std::vector<float> numbers) {
    std::sort(numbers.begin(), numbers.end());
    float min_diff = std::numeric_limits<float>::max();
    float closest_pair[2];

    for (int i = 0; i < numbers.size() - 1; i++) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < min_diff) {
            min_diff = diff;
            closest_pair[0] = numbers[i];
            closest_pair[1] = numbers[i + 1];
        }
    }
    return std::vector<float>(closest_pair, closest_pair+2);
}

int main() {
    std::vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    std::vector<float> result = find_closest_elements(numbers);
    for (float num : result) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

std::vector<float> find_closest_elements(std::vector<float> numbers) {
    std::sort(numbers.begin(), numbers.end());
    float min_diff = std::numeric_limits<float>::max