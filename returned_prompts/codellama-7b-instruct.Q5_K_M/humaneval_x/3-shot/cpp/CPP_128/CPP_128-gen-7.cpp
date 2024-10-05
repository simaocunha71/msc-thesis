    int sum=0;
    if (arr.size()==0)
    return -32768;
    int product=1;
    int i;
    for (i=0;i<arr.size();i++){
        if (arr[i]>0)
        product*=1;
        else if (arr[i]<0)
        product*=-1;
        else
        product*=0;
        sum+=abs(arr[i]);
    }
    return product*sum;
}


