    sort(numbers.begin(),numbers.end());
    vector<int>::iterator unique_end=unique(numbers.begin(),numbers.end());
    numbers.erase(unique_end,numbers.end());
    return numbers;
}



