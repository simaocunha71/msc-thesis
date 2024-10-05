    int i;
    int len=arr.size();
    int j;
    int flag=0;
    for (i=0;i<len-1;i++)
    {
        if (arr[i]>arr[i+1])
        {
            for (j=i+1;j<len;j++)
            {
                if (arr[j]<arr[j-1])
                {
                    flag=1;
                    break;
                }
            }
            if (flag==0)
            return 0;
        }
    }
    return 1;
}


