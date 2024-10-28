    float min_num = *min_element(numbers.begin(), numbers.end());
    float max_num = *max_element(numbers.begin(), numbers.end());
    vector<float> rescaled;
    for (int i = 0; i < numbers.size(); i++) {
        rescaled.push_back((numbers[i] - min_num) / (max_num - min_num));
    }
    return rescaled;
}  // returns a vector of floats
