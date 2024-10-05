    vector<int> result;
    int i;
    int n=numbers.size();
    for (i=0;i<n;i++)
    {
        result.push_back(numbers[i]);
        if (i!=n-1) result.push_back(delimeter);
    }
    return result;
}


