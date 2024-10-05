    vector<int> max_nums;
    int max_number=numbers[0];
    max_nums.push_back(max_number);
    for(int i=1;i<numbers.size();i++){
        if(numbers[i]>max_number){
            max_number=numbers[i];
        }
        max_nums.push_back(max_number);
    }
    return max_nums;
}


