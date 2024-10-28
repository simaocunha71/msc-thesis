    int i,n=array.size();
    int first_index=0,last_index=n-1;
    int sum=array[first_index]+array[last_index];
    if (sum%2==0)
    sort(array.begin(),array.end(),greater<int>());
    else sort(array.begin(),array.end());
    return array;
}


