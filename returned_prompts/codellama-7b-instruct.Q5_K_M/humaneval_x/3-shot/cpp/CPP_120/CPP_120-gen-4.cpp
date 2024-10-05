    vector<int> ans;
    vector<int> sorted_arr=arr;
    sort(sorted_arr.begin(),sorted_arr.end());
    for (int i=0;i<k;i++)
    ans.push_back(sorted_arr[sorted_arr.size()-k+i]);
    return ans;
}


