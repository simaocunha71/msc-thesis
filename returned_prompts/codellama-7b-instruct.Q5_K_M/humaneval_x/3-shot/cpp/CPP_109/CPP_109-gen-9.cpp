    int i,j;
    bool flag=false;
    for (i=1;i<arr.size();i++)
    if (arr[i]<arr[i-1])
    {
        flag=true;
        for (j=i;j<arr.size();j++)
        if (arr[j]<arr[j-1])
        {
            swap(arr[j],arr[j-1]);
        }
        if (flag)
        {
            swap(arr[arr.size()-1],arr[i-1]);
            return true;
        }
        else 
        return false;
    }
    return true;
}


