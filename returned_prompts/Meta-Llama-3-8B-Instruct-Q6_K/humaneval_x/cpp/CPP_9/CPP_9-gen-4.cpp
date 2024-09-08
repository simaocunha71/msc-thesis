    vector<int> result;
    int max_element = numbers[0];
    result.push_back(max_element);

    for(int i = 1; i < numbers.size(); i++){
        if(numbers[i] > max_element){
            max_element = numbers[i];
        }
        result.push_back(max_element);
    }
    return result;
}
int main(){
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

