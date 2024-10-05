    int i;
    int min=arr[0];
    int index=0;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0)
        {
            if (arr[i]<min)
            {
                index=i;
                min=arr[i];
            }
        }
    }
    if (index==0 && min==arr[0] && min%2!=0)
    {
        return {};
    }
    else{
        vector<int> output={min,index};
        return output;
    }
}

