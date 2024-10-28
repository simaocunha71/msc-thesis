    vector<int> ans;
    vector<int>::iterator it;
    sort(arr.begin(),arr.end());
    it=ans.begin();
    for (int i=arr.size()-1;i>=arr.size()-k;i--)
    {
        *it=arr[i];
        it++;
    }
    return ans;
}

