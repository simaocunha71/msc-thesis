    vector<int> output;
    if (arr.size()==0)
    return output;
    int min_value=INT_MAX;
    int min_index;
    int i;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0 && arr[i]<min_value){
        min_value=arr[i];
        min_index=i;
    }
    output.push_back(min_value);
    output.push_back(min_index);
    return output;
}


