    sort(numbers.begin(), numbers.end());
    vector<int>::iterator it;
    it = numbers.begin();
    while (it != numbers.end()) {
        if ((it != numbers.begin()) && (*it == *(it-1))) {
            it = numbers.erase(it);
        } else {
            ++it;
        }
    }
    return numbers;
}


