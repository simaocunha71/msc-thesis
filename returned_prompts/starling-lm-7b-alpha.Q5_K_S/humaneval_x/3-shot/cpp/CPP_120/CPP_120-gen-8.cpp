    vector<int> ans;
    int i;
    sort(arr.begin(),arr.end(),greater<int>());
    for (i=0;i<k;i++)
    ans.push_back(arr[i]);

    return ans;
}



