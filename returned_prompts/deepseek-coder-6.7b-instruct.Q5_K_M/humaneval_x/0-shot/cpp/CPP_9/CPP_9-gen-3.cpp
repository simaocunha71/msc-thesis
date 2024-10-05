    vector<int> max_numbers;
    int max = numbers[0];
    max_numbers.push_back(max);
    for(int i=1; i<numbers.size(); i++){
        if(numbers[i] > max){
            max = numbers[i];
        }
        max_numbers.push_back(max);
    }
    return max_numbers;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> max_numbers = rolling_max(numbers);
    for(int i=0; i<max_numbers.size(); i++){
        printf("%d ",max_numbers[i]);
    }
    return 0;
}

This program will print: 1 2 3 3 3 4 4.

Explanation:
The program generates a new vector with the rolling maximum values from the given vector. The function rolling_max takes in a vector of integers, initializes the maximum to the first element of the vector, and then iterates through the vector. If the current element is greater than the maximum, the maximum is updated. The maximum value is then added to the new vector. The function returns the new vector. The main function tests the rolling_max function with the vector {1, 2, 3, 2, 3, 4, 2}, and prints the result.
*/


```


```cpp

// 1.2

/*
