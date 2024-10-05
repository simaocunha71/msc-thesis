    int sum=0;
    int i;
    for (i=0;i<array.size();i++)
    sum+=array[i];
    if (sum%2==1)
    sort(array.begin(), array.end());
    else
    sort(array.begin(), array.end(), greater<int>());
    return array;
}


