    if (arr.size()==0) return -32768;
    int sum=0;
    int product=1;
    for (int i=0;i<arr.size();i++)
    {
        product*=arr[i]/abs(arr[i]);
        sum+=abs(arr[i]);
    }
    return sum*product;
}


