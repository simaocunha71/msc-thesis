    vector<int> result;
    int i;
    for (i=0;i<arr.size();i++)
    {
        result.push_back(arr[i]);
    }
    sort(result.begin(),result.end());
    return result;
}


