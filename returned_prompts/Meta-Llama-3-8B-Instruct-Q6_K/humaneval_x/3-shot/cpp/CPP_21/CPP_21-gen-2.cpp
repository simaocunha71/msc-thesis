    float min_val = *min_element(numbers.begin(), numbers.end());
    float max_val = *max_element(numbers.begin(), numbers.end());
    vector<float> result;
    for (int i = 0; i < numbers.size(); i++) {
        result.push_back((numbers[i] - min_val) / (max_val - min_val));
    }
    return result;
}  // this function assumes that the input vector has at least two elements
// if the vector has only one element, you would get a runtime error
// you might want to add a check for that case.