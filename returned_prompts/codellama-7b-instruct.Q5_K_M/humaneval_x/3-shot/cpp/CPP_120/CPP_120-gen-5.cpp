    vector<int> ans;
    sort(arr.begin(), arr.end());
    for (int i=arr.size()-1;i>=0 && k>0;i--,k--)
    ans.push_back(arr[i]);
    return ans;
}




