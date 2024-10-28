    vector<int> temp;
    for (int i=0;i<arr.size();i++)
    if (arr[i]>9 && arr[i]<100)
    temp.push_back(arr[i]);
    sort(temp.begin(),temp.end());
    reverse(temp.begin(),temp.end());
    return temp;
}



