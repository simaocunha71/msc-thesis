    int i,j;
    int min=0;
    for (i=0;i<arr.size();i++)
        for (j=i+1;j<arr.size();j++)
        {
            if (arr[i]!=arr[j])
                min+=1;
        }
    return min;
}

