    int i,j;
    
    for (i=0;i<arr.size()-1;i++)
    {
        for (j=i+1;j<arr.size();j++)
        {
            if (arr[i]>arr[j])
            {
                return false;
            }
        }
    }
    return true;
}