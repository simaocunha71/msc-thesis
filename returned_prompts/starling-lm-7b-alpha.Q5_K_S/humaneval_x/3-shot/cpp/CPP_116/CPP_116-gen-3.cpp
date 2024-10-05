    vector<int> sorted_arr;
    int i,j;
    int size=arr.size();
    for (i=0;i<size;i++)
    {
        int count=0;
        int temp=arr[i];
        while (temp>0)
        {
        temp=temp/2;
        count+=1;
        }
        sorted_arr.push_back(count);
    }
    sort(sorted_arr.begin(),sorted_arr.end());
    for (i=0;i<size;i++)
    {
        for (j=0;j<size;j++)
        {
        if (sorted_arr[i]==arr[j])
        {
        arr[j]=i;
        }
        }
    }
    return arr;
}



