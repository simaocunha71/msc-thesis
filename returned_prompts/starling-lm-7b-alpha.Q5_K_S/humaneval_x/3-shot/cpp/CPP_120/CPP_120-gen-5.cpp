    vector<int> ans;
    sort(arr.rbegin(),arr.rend());
    for (int i=0;i<k;i++)
    ans.push_back(arr[i]);
    return ans;
}



