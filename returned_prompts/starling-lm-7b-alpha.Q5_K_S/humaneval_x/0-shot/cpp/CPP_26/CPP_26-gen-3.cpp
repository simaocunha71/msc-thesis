    vector<int> result;
    result.clear();
    result.reserve(numbers.size());
    result.push_back(numbers[0]);
    for(int i = 1; i < numbers.size(); i++)
        if(result.back() != numbers[i])
            result.push_back(numbers[i]);
    return result;
}

B:
    vector<int> result;
    result.clear();
    result.reserve(numbers.size());
    for(int i = 0; i < numbers.size(); i++)
        if(result.find(numbers[i]) == result.end())
            result.push_back(numbers[i]);
    return result;
}

C:
    vector<int> result;
    result.clear();
    result.reserve(numbers.size());
    sort(numbers.begin(), numbers.end());
    result.push_back(numbers[0]);
    for(int i = 1; i < numbers.size(); i++)
        if(numbers[i] != result.back())
            result.push_back(numbers[i]);
    return result;
}

D:
    vector<int> result;
    result.clear();
    result.reserve(numbers.size());
    sort(numbers.begin(), numbers.end());
    result.push_back(numbers[0]);
    for(int i = 1; i < numbers.size(); i++)
        if(numbers[i] != result.back() && result.back() != numbers[i - 1])
            result.push_back(numbers[i]);
    return result;
}

E:
    vector<int> result;
    result.clear();
    result.reserve(numbers.size());
    sort(numbers.begin(), numbers.end());
    result.push_back(numbers[0]);
    for(int i = 1; i < numbers.size(); i++)
        if(numbers[i] != result.back() && result.back() != numbers[i - 1] && result.back() != numbers