    int i,j;
    vector<int> arr2=arr;
    int a=arr[0];
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]!=i+1)
        {
            return false;
        }
    }
    return true;
} 

