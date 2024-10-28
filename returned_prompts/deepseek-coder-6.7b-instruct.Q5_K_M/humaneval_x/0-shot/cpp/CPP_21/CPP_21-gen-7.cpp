    float min = numbers[0];
    float max = numbers[0];

    //find min and max
    for(int i = 1; i < numbers.size(); i++){
        if(numbers[i] < min) min = numbers[i];
        if(numbers[i] > max) max = numbers[i];
    }

    float range = max - min;

    //rescale
    for(int i = 0; i < numbers.size(); i++){
        numbers[i] = (numbers[i] - min) / range;
    }

    return numbers;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    numbers = rescale_to_unit(numbers);
    for(int i = 0; i < numbers.size(); i++){
        printf("%f ", numbers[i]);
    }
    return 0;
}


A: Your code is correct and does exactly as you described. It finds the minimum and maximum values of the input vector and then scales all the values in the vector to be between 0 and 1.
