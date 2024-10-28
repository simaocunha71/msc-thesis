    vector<int>::iterator new_end;
    new_end = unique(numbers.begin(), numbers.end());
    numbers.erase(new_end, numbers.end());
    return numbers;
}



