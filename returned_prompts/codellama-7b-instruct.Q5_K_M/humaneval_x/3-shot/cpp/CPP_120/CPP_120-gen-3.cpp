    vector<int> result;
    sort(arr.begin(),arr.end());
    for (int i=arr.size()-1;i>=0;i--)
    {
        result.push_back(arr[i]);
        if (result.size()==k)
        break;
    }
    return result;
}


