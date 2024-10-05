    vector<int> result;
    for (int i=0;i<arr.size();i++)
    {
        if (arr[i]>=1 && arr[i]<=9)
        result.push_back(arr[i]);
    }
    sort(result.begin(),result.end());
    reverse(result.begin(),result.end());
    vector<string> ans;
    for (int i=0;i<result.size();i++)
    {
        ans.push_back("One");
    }
    return ans;
}


