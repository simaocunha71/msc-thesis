    vector<int> result;
    int max_num = numbers[0];
    result.push_back(max_num);
    for(int i = 1; i < numbers.size(); i++){
        if(numbers[i] > max_num){
            max_num = numbers[i];
        }
        result.push_back(max_num);
    }
    return result;
}

int main(){
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
The rolling_max function in the above program takes a vector of integers as input and returns a new vector containing the rolling maximum elements found until the given moment in the sequence. In the main function, we test this function with a given vector of integers. The output of the program is the rolling maximum elements found in the sequence. The time complexity of this function is O(n), where n is the size of the input vector. The space complexity is also O(n) as we are creating a new vector to store the result.