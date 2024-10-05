    for (int i=0;i<arr.size();i++)
    arr[i]=__builtin_popcount(arr[i]);
    sort(arr.begin(),arr.end());
    return arr;
}



