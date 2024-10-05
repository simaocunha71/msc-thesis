    vector<int> new_arr;
    for (int i=0;i<arr.size();i++)
    if (arr[i]>9)
    new_arr.push_back(arr[i]);
    sort(new_arr.begin(),new_arr.end());
    reverse(new_arr.begin(),new_arr.end());
    return new_arr;
}


