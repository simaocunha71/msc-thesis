    vector<int> sorted;
    for (int i=0;i<arr.size();i++)
    {
        int count=0;
        while (arr[i]>0)
        {
            count++;
            arr[i]=arr[i]-int(arr[i]/2);
        }
        sorted.push_back(count);
    }
    sort(sorted.begin(), sorted.end());
    for (int i=0;i<arr.size();i++)
    arr[i]=sorted[i];
    return arr;
}


