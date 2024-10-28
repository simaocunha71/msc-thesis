    if (array.size()==0)
    return array;

    int i;
    int sum=0;
    for (i=0;i<array.size();i++)
    sum+=array[i];

    if ((sum%2)==0)
    sort(array.begin(), array.end(), greater<int>());
    else
    sort(array.begin(), array.end());

    return array;
}



