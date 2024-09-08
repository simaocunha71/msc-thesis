    vector<int> result;
    int max_val = INT_MIN;
    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] > max_val){
            max_val = numbers[i];
        }
        result.push_back(max_val);
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

