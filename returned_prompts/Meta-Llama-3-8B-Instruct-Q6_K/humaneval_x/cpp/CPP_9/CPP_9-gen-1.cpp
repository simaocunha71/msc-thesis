    vector<int> result;
    int max = numbers[0];
    result.push_back(max);
    for(int i=1; i < numbers.size(); i++){
        if(numbers[i] > max){
            max = numbers[i];
        }
        result.push_back(max);
    }
    return result;
}

B:
    vector<int> result;
    int max = INT_MIN;
    for(int i = 0; i < numbers.size(); i++){
        max = max > numbers[i] ? max : numbers[i];
        result.push_back(max);
    }
    return result;
}

C:
    vector<int> result;
    int max = numbers[0];
    for(int i = 1; i < numbers.size(); i++){
        result.push_back(max = max > numbers[i] ? max : numbers[i]);
    }
    return result;
}

D:
    vector<int> result;
    int max = numbers[0];
    for(int i = 0; i < numbers.size(); i++){
        result.push_back(max);
        max = max > numbers[i] ? max : numbers[i];
    }
    return result;
}
int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

Output:
1 2 3 3 3 4 4
Explanation:
The task is to create a function that takes a vector of integers as input and returns a new vector where each element is the maximum value found in the input vector up to that point.

The function rolling_max() is implemented in four different ways in the code provided. The correct implementation is option B.

In option B, the variable max is initialized to INT_MIN (the smallest possible integer value) to ensure that the first element of the input vector is always considered the maximum. Then, for each element in the input vector, the function checks if the current element is greater than the maximum found so far, and updates the maximum if necessary. The updated maximum is then added to the result vector.

The other options do not correctly implement the rolling maximum function. Option A updates the maximum only after the entire input vector has been processed, which is not correct. Option C updates the maximum in a single statement, but this is