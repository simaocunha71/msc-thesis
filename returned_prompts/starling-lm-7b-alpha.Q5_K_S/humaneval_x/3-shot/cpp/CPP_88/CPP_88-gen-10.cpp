    int i;
    int n=array.size();
    if ((array[0]+array[n-1])%2==0)
    sort(array.begin(),array.end(),greater<int>());
    else
    sort(array.begin(),array.end());
    return array;
}



