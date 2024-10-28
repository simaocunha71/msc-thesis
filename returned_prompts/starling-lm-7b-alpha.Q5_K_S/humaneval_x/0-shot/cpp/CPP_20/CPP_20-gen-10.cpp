    float diff = -1;
    float min1 = 1000000000;
    float min2 = 1000000000;
    int min1_index = -1;
    int min2_index = -1;
    for(int i = 0; i < numbers.size(); ++i){
        float diff = abs(numbers[i] - numbers[i + 1]);
        if(diff < min1){
            min1 = diff;
            min1_index = i;
        }
        if(diff > min1 && diff < min2){
            min2 = diff;
            min2_index = i;
        }
    }
    vector<float> result;
    result.push_back(numbers[min1_index]);
    result.push_back(numbers[min2_index]);
    return result;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    printf("%f %f", result[0], result[1]);
    return 0;
}



















































































































































































































