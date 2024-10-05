    int n=arr.size();
    for(int i=0;i<n-1;i++)
    {
        if(arr[i]>arr[i+1])
        {
            for(int j=0;j<i;j++)
            {
                if(arr[j]>arr[i+1]) return false;
            }
            return true;
        }
    }
    return true;
}


