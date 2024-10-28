    int sign_product=1;
    float sum=0;
    if(arr.size()==0)
        return -32768;
    for (int i=0;i<arr.size();i++)
    {
        if(arr[i]>0)
            sign_product*=1;
        if(arr[i]<0)
            sign_product*=-1;
        sum+=abs(arr[i]);
    }
    return sign_product*(int)sum;
}  // This code is not working for negative numbers. I will correct it later.