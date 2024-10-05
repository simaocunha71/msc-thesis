    vector<int> max_numbers;
    int max_so_far = numbers[0];
    max_numbers.push_back(max_so_far);
    for(int i=1;i<numbers.size();i++){
        if(numbers[i]>max_so_far){
            max_so_far = numbers[i];
        }
        max_numbers.push_back(max_so_far);
    }
    return max_numbers;
}


