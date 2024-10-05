    sort(numbers.begin(),numbers.end());
    auto last=unique(numbers.begin(),numbers.end());
    numbers.erase(last,numbers.end());
    return numbers;
}


