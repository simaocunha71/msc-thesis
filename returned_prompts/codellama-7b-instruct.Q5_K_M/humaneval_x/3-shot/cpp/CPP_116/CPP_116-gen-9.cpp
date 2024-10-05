    vector<int> sorted_array;
    vector<int> temp;
    int i;
    for (i=0;i<arr.size();i++)
    {
        int ones=0;
        int j;
        for (j=0;j<sizeof(arr[i]);j++)
        if (arr[i][j]==1)
        ones+=1;
        temp.push_back(ones);
        temp.push_back(arr[i]);
    }
    sort(temp.begin(),temp.end());
    int k=0;
    for (i=0;i<temp.size();i++)
    if (temp[i]!=temp[k])
    sorted_array.push_back(temp[i+1]);
    k+=2;
    return sorted_array;
}


