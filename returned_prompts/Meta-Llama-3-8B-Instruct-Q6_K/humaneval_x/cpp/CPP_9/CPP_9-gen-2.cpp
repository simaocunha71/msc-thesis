    vector<int> result;
    int max = numbers[0];
    result.push_back(max);
    for(int i=1; i<numbers.size(); i++){
        if(numbers[i] > max){
            max = numbers[i];
        }
        result.push_back(max);
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}