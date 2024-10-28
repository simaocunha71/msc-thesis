    sort(numbers.begin(), numbers.end());
    vector<int>::iterator it = numbers.begin();
    while (it != numbers.end()) {
        if ((it+1) != numbers.end() && *it == *(it+1)) {
            it = numbers.erase(it);
        } else {
            ++it;
        }
    }
    return numbers;
}


