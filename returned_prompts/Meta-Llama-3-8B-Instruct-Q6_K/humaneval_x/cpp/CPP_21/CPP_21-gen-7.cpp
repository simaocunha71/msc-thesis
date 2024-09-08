    vector<float> result;
    if(numbers.size() < 2) return result; // check if vector has at least two elements
    float min_val = *min_element(numbers.begin(), numbers.end()); // find the smallest number
    float max_val = *max_element(numbers.begin(), numbers.end()); // find the largest number
    for(float num : numbers){ // iterate through each number in the vector
        float scaled = (num - min_val) / (max_val - min_val); // apply the linear transform
        result.push_back(scaled); // add the scaled number to the result vector
    }
    return result; // return the result vector
}

