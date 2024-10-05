    int i,product=1,magnitude;
    for (i=0;i<arr.size();i++)
    {
        magnitude=abs(arr[i]);
        product*=arr[i]/magnitude;
    }
    return product;
}


