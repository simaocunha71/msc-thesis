    int i,min=10000000,min_index;
    vector<int> ret;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0 && arr[i]<min){
        min=arr[i];
        min_index=i;
    }
    ret.push_back(min);
    ret.push_back(min_index);
    return ret;
}


