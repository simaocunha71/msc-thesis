    int sum=0;
    for (int i=0;i<array.size();i++)
    sum+=array[i];
    bool odd=sum%2;
    if (odd==true)
    sort(array.begin(), array.end());
    else
    sort(array.begin(), array.end(), greater<int>());
    return array;
}


