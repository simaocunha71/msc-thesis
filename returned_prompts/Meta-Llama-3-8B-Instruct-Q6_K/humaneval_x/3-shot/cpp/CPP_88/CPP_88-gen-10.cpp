    int sum=*(array.begin())+*(array.end()-1);
    if(sum%2==0)
    {
        sort(array.begin(),array.end(),greater<int>());
    }
    else
    {
        sort(array.begin(),array.end());
    }
    return array;
}