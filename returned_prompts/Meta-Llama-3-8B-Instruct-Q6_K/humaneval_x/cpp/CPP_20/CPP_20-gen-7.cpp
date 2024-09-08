    float min_diff = std::numeric_limits<float>::max();
    float closest_pair[2] = {0.0, 0.0};

    for(int i = 0; i < numbers.size(); i++){
        for(int j = i + 1; j < numbers.size(); j++){
            float diff = std::abs(numbers[i] - numbers[j]);
            if(diff < min_diff){
                min_diff = diff;
                closest_pair[0] = numbers[i];
                closest_pair[1] = numbers[j];
            }
        }
    }

    vector<float> result;
    result.push_back(closest_pair[0]);
    result.push_back(closest_pair[1]);
    return result;
}

int main(int argc, char const *argv[]) {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    printf("(%f, %f)\n", result[0], result[1]);
    return 0;
}
