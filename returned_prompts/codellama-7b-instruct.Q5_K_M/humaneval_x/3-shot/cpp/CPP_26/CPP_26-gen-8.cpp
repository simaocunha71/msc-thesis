    sort(numbers.begin(), numbers.end());
    auto it=unique(numbers.begin(), numbers.end());
    numbers.resize(it-numbers.begin());
    return numbers;
}


