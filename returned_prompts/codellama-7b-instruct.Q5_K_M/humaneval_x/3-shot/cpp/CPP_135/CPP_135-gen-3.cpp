    int i,j;
    int max=0;
    int current;
    for (i=0;i<arr.size();i++)
    {
        current=arr[i];
        for (j=i+1;j<arr.size();j++)
        {
            if (arr[j]>current)
            {
                max=j;
                break;
            }
        }
    }
    if (max==0)
    return -1;
    else
    return max-1;
}


