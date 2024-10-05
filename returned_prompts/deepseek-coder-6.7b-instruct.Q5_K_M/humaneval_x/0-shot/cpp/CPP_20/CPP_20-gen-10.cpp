    sort(numbers.begin(), numbers.end());
    int size = numbers.size();
    float min_diff = numbers[1] - numbers[0];
    int min_index = 0;
    for (int i = 1; i < size - 1; i++){
        float diff = numbers[i+1] - numbers[i];
        if (diff < min_diff){
            min_diff = diff;
            min_index = i;
        }
    }
    vector<float> closest_elements;
    closest_elements.push_back(numbers[min_index]);
    closest_elements.push_back(numbers[min_index+1]);
    return closest_elements;
}

*/

//main function
int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> closest = find_closest_elements(numbers);
    printf("(%f, %f)", closest[0], closest[1]);
    return 0;
}

//end of main

//end of code

//src/main/resources/cpp/find_closest_elements.cpp
/*
