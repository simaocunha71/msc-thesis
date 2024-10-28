    vector<int> sorted_arr;
    vector<int> ignore_arr;
    vector<string> by_length_arr;
    int i;
    for (i=0;i<arr.size();i++)
    if (arr[i]>=1 && arr[i]<=9)
    sorted_arr.push_back(arr[i]);
    else
    ignore_arr.push_back(arr[i]);
    sort(sorted_arr.begin(),sorted_arr.end());
    reverse(sorted_arr.begin(),sorted_arr.end());
    for (i=0;i<sorted_arr.size();i++)
    by_length_arr.push_back(
        map<int,string>::iterator()->second);
    return by_length_arr;
}


