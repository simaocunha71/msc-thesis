    vector<float> result;
    float min = 0;
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (fabs(numbers[i] - numbers[j]) < min || min == 0) {
                min = fabs(numbers[i] - numbers[j]);
                result.push_back(numbers[i]);
                result.push_back(numbers[j]);
            }
        }
    }
    return result;
}
