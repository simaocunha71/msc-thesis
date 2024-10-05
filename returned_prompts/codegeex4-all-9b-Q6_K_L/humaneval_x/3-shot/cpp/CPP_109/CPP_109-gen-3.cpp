    int i,j;
    int max=0;
    for (i=0;i<arr.size();i++)
    if (arr[i]>max)
    max=arr[i];

    for (i=0;i<arr.size();i++)
    {
        j=i;
        while (j<arr.size())
        {
            if (arr[j]<max)
            return false;
            j++;
        }
    }
    return true;
}

