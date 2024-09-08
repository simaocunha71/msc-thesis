    vector<int> unique_numbers = numbers;
    sort(unique_numbers.begin(), unique_numbers.end());
    unique_numbers.erase(unique(unique_numbers.begin(), unique_numbers.end()), unique_numbers.end());
    return unique_numbers;
}
B:
    vector<int> unique_numbers;
    for(int i = 0; i < numbers.size(); i++){
        bool is_unique = true;
        for(int j = 0; j < unique_numbers.size(); j++){
            if(unique_numbers[j] == numbers[i]){
                is_unique = false;
                break;
            }
        }
        if(is_unique){
            unique_numbers.push_back(numbers[i]);
        }
    }
    return unique_numbers;
}
C:
    vector<int> unique_numbers;
    for(int i = 0; i < numbers.size(); i++){
        bool is_duplicate = false;
        for(int j = 0; j < unique_numbers.size(); j++){
            if(unique_numbers[j] == numbers[i]){
                is_duplicate = true;
                break;
            }
        }
        if(!is_duplicate){
            unique_numbers.push_back(numbers[i]);
        }
    }
    return unique_numbers;
}
int main() {
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> unique_numbers = remove_duplicates(numbers);
    for(int i = 0; i < unique_numbers.size(); i++){
        printf("%d ", unique_numbers[i]);
    }
    printf("\n");
    return 0;
}

