    vector<int> result;
    int max = numbers[0];
    result.push_back(max);

    for (int i = 1; i < numbers.size(); i++){
        if (numbers[i] > max){
            max = numbers[i];
        }
        result.push_back(max);
    }
    return result;
}

int main(){
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for (int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

Explanation:
The function `rolling_max` takes in a vector of integers and returns a new vector where each element is the maximum element found in the original vector up to that point. This is done by initializing the maximum as the first element in the vector, then iterating through the vector. If the current element is greater than the current maximum, it replaces the maximum. After each iteration, the current maximum is added to the result vector. The result vector is then returned.

The `main` function is the driver of the program. It creates a vector of integers, calls `rolling_max` on it, and then prints the result.
*/

