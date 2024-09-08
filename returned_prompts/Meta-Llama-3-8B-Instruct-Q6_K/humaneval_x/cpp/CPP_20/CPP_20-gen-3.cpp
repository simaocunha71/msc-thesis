    float min_diff = numeric_limits<float>::max();
    float closest_elements[2];
    for(int i = 0; i < numbers.size(); i++){
        for(int j = i+1; j < numbers.size(); j++){
            float diff = abs(numbers[i] - numbers[j]);
            if(diff < min_diff){
                min_diff = diff;
                closest_elements[0] = numbers[i];
                closest_elements[1] = numbers[j];
            }
        }
    }
    return vector<float>(closest_elements, closest_elements + 2);
}
int main()
{
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    printf("(%f, %f)\n", result[0], result[1]);
    return 0;
}

