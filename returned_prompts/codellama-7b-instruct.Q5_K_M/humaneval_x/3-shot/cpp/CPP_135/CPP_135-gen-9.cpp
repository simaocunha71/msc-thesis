    int i,j;
    int max_index=-1;
    int max_val=0;
    for (i=0;i<arr.size();i++)
    {
        for (j=i+1;j<arr.size();j++)
        {
            if (arr[i]<=arr[j])
            {
                if (arr[i]>max_val)
                {
                    max_index=i;
                    max_val=arr[i];
                }
                break;
            }
        }
    }
    return max_index;
}


