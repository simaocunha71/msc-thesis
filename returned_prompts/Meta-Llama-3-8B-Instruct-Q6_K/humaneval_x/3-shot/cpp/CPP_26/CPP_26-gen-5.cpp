    vector<int> result;
    for(int i: numbers)
    {
        if(find(result.begin(), result.end(), i) == result.end())
        {
            result.push_back(i);
        }
    }
    return result;
}

