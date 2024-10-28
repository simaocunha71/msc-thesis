    int sum=0;
    for (int i=0;i<array.size();i++)
    sum+=array[i];

    if (sum%2==0)
    sort(array.begin(),array.end());
    else
    sort(array.begin(),array.end(),greater<int>());
    return array;
}


