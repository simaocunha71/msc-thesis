    sort(numbers.begin(),numbers.end());
    vector<int>::iterator it=unique(numbers.begin(),numbers.end());
    numbers.resize(distance(numbers.begin(),it));
    return numbers;
}



