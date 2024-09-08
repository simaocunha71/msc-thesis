    // check if there are at least two elements
    if (numbers.size() < 2) {
        throw std::invalid_argument("Vector must have at least two elements");
    }

    // find the smallest and largest numbers
    float min_val = *min_element(numbers.begin(), numbers.end());
    float max_val = *max_element(numbers.begin(), numbers.end());

    // create a new vector with the rescaled values
    vector<float> result;
    for (float num : numbers) {
        float scaled_num = (num - min_val) / (max_val - min_val);
        result.push_back(scaled_num);
    }

    return result;
}
