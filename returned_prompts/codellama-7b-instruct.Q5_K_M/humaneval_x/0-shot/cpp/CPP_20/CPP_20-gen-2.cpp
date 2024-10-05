    vector<float> closest_numbers;
    int closest_index = 0;
    int second_closest_index = 0;
    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] - numbers[closest_index] < numbers[i] - numbers[second_closest_index]){
            second_closest_index = closest_index;
            closest_index = i;
        } else if(numbers[i] - numbers[second_closest_index] < numbers[i] - numbers[closest_index]){
            second_closest_index = i;
        }
    }
    closest_numbers.push_back(numbers[closest_index]);
    closest_numbers.push_back(numbers[second_closest_index]);
    return closest_numbers;
}
int main(void){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> closest_numbers = find_closest_elements(numbers);
    for(int i = 0; i < closest_numbers.size(); i++){
        printf("%.1f, ", closest_numbers[i]);
    }
    return 0;
}

