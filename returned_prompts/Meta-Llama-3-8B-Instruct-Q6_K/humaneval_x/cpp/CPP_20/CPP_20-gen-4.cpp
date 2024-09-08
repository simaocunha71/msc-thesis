    vector<float> result;
    float min_diff = numeric_limits<float>::max();
    float closest_numbers[2];
    for(int i = 0; i < numbers.size(); i++){
        for(int j = i+1; j < numbers.size(); j++){
            float diff = abs(numbers[i] - numbers[j]);
            if(diff < min_diff){
                min_diff = diff;
                closest_numbers[0] = numbers[i];
                closest_numbers[1] = numbers[j];
            }
        }
    }
    result.push_back(closest_numbers[0]);
    result.push_back(closest_numbers[1]);
    return result;
}
int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    for (float num : result) {
        printf("%f\n", num);
    }
    return 0;
}
B:
    vector<float> find_closest_elements(vector<float> numbers){
    if (numbers.size() < 2) {
        throw runtime_error("Vector must have at least two elements");
    }
    sort(numbers.begin(), numbers.end());
    float min_diff = numeric_limits<float>::max();
    float closest_numbers[2];
    for(int i = 0; i < numbers.size() - 1; i++){
        float diff = numbers[i+1] - numbers[i];
        if(diff < min_diff){
            min_diff = diff;
            closest_numbers[0] = numbers[i];
            closest_numbers[1] = numbers[i+1];
        }
    }
    return {closest_numbers[0], closest_numbers[1]};
}
int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    for (float num : result) {
        printf("%f\n", num);
    }
    return 0;
}

C:
    vector<float> find_closest_elements(vector<float> numbers){
    if (numbers.size() < 2) {
        throw runtime_error("Vector must have at least two elements");
    }
    sort(numbers.begin(), numbers.end());
    vector<float> closest_numbers;
    float min_diff = numeric_limits<float>::max();
    for(int i = 0;