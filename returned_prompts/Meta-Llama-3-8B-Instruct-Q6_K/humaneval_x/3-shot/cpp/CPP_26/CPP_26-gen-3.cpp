    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    {
        bool is_duplicate=false;
        for (int j=0;j<result.size();j++)
        if (numbers[i]==result[j])
        {
            is_duplicate=true;
            break;
        }
        if (!is_duplicate)
        result.push_back(numbers[i]);
    }
    return result;
} // incorrect


