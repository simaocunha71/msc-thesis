    int i,j;
    int min=arr[0];
    int max=arr[0];
    for (i=1;i<arr.size();i++)
    {
        if (arr[i]<min)
        {
            min=arr[i];
        }
    }
    for (i=1;i<arr.size();i++)
    {
        if (arr[i]>max)
        {
            max=arr[i];
        }
    }
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]!=i+min)
        {
            return false;
        }
    }
    return true;
}

