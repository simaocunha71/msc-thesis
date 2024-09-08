    if (numbers.size() < 2) {
        return numbers; // return the vector as it is
    }

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
    vector<float> result(2);
    result[0] = closest_pair[0];
    result[1] = closest_pair[1];
    return result;
}
int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    for(auto i : result){
        printf("%f ",i);
    }
    printf("\n");
    return 0;
}
