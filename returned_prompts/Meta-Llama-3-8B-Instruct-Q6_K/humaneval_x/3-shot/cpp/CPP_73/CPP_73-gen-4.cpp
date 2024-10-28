    int changes=0;
    for(int i=0;i<arr.size();i++)
    {
        if (i<arr.size()-i-1&&arr[i]!=arr[arr.size()-i-1])
        {
            changes++;
        }
    }
    return changes;
}