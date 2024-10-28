    int i,j,changes=0;
    for (i=0;i<arr.size();i++)
    {
        for (j=0;j<arr.size();j++)
        {
            if (i!=j && arr[i]!=arr[j])
            {
                arr[i]=arr[j];
                changes+=1;
            }
        }
    }
    return changes;
}


