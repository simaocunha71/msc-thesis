    vector<int> temp;
    sort(arr.begin(),arr.end());
    for (int i=0;i<k;i++)
    temp.push_back(arr[arr.size()-k+i]);
    return temp;
}



