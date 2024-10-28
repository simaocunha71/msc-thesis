    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    {
        result.push_back(numbers[i]);
        result.push_back(delimeter);
    }
    result.pop_back();
    return result;
}


