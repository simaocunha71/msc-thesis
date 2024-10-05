/*
From a supplied vector of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).
*/

    vector<float> closest_numbers;
    closest_numbers.reserve(2);

    float closest_difference = abs(numbers[0] - numbers[1]);

    for (int i = 0; i < numbers.size() - 1; i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            float difference = abs(numbers[i] - numbers[j]);
            if (difference < closest_difference) {
                closest_difference = difference;
                closest_numbers.clear();
                closest_numbers.push_back(numbers[i]);
                closest_numbers.push_back(numbers[j]);
            }
        }
    }
    return closest_numbers;
}

int main() {
    vector<float> nums = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> closest_nums = find_closest_elements(nums);
    printf("(%0.1f, %0.1f)\n", closest_nums[0], closest_nums[1]);

    nums = {1.0, 2.0, 3.0, 4.0, 5.0, 2.0};
    closest_nums = find_closest_elements(nums);
    printf("(%0.1f, %0.1f)\n", closest_nums[0], closest_nums[1]);

    return 0;
}
