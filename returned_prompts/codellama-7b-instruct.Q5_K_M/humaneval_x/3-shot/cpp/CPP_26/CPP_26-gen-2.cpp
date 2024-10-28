    sort(numbers.begin(),numbers.end());
    vector<int>::iterator it=unique(numbers.begin(),numbers.end());
    numbers.resize(it-numbers.begin());
    return numbers;
}


