    int sum=0;
    int first=array[0];
    int last=array[array.size()-1];
    sum=first+last;
    if (sum%2==0)
    {
        sort(array.begin(),array.end(),greater<int>());
    }
    else
    {
        sort(array.begin(),array.end());
    }
    return array;
}