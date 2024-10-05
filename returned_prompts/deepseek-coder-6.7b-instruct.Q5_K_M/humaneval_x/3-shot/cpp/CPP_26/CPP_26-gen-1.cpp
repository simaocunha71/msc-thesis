    vector<int> result;
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size(); i++)
    {
        while (i + 1 < numbers.size() && numbers[i] == numbers[i + 1])
        {
            i++;
        }
        result.push_back(numbers[i]);
    }
    return result;
}

