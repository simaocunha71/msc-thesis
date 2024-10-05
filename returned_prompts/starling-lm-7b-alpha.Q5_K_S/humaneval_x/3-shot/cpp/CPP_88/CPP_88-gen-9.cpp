    int i,n=array.size()-1;
    if (array[0]+array[n]%2==0)
    sort(array.begin(),array.end(),greater<int>());
    else
    sort(array.begin(),array.end());
    return array;
}



