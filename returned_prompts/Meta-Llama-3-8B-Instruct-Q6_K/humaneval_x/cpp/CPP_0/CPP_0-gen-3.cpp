bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            float diff = abs(numbers[i] - numbers[j]);
            if (diff < threshold) {
                return true;
            }
        }
    }
    return false;
}

