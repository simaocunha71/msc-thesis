    if ((array.size()>0) && ((array[0]+array.back())%2==0))
        sort(array.begin(), array.end());
    else
        sort(array.begin(), array.end(), greater<int>());
    return array;
}