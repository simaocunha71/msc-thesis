    vector<int> odd_numbers;
    while(n != 1){
        if(n % 2 != 0){
            odd_numbers.push_back(n);
        }
        n = n % 2 ? n*3 + 1 : n / 2;
    }
    odd_numbers.push_back(1);
    sort(odd_numbers.begin(), odd_numbers.end());
    return odd_numbers;
}


