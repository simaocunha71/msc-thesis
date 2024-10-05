    int min_index;
    int min_index2;
    float min = 1000000000;
    float min2 = 1000000000;
    for(int i = 0; i < numbers.size(); i++){
        for(int j = 0; j < numbers.size(); j++){
            if(numbers[i] != numbers[j]){
                float temp = fabs(numbers[i] - numbers[j]);
                if(temp < min){
                    min2 = min;
                    min = temp;
                    min_index = j;
                    min_index2 = i;
                }else if(temp < min2){
                    min2 = temp;
                    min_index2 = j;
                }
            }
        }
    }
    vector<float> result;
    result.push_back(numbers[min_index]);
    result.push_back(numbers[min_index2]);
    return result;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> result = find_closest_elements(numbers);
    printf("%.2f %.2f\n", result[0], result[1]);
    return 0;
}



/*
The code takes a vector of numbers as input, and then loops over each element in the vector to compare it to all other
elements in the vector. It uses the abs function to calculate the absolute difference in value between each pair of elements,
and keeps track of the smallest and second smallest differences found. Once it has found the smallest two differences, it
stores the corresponding elements in the result vector and returns it.

In the main function, a test vector of numbers is created and passed to the find_closest_elements function. The result vector
is then printed out to the console, with the two closest elements printed in order, with their values rounded to two decimal
places.

The expected output for the provided test cases is (2.0, 2.2)