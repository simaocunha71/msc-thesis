    int i,j,temp;
    for (i=0;i<arr.size()-1;i++)
    {
        for (j=i+1;j<arr.size();j++)
        {
            if (arr[j]<arr[i])
            {
                temp=arr[j];
                arr[j]=arr[i];
                arr[i]=temp;
                j=i;
            }
        }
    }
    return true;
}


