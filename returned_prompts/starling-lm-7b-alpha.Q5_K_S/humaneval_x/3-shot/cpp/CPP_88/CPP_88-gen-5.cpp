    int i;
    int total_sum=array[0]+array[array.size()-1];
    if (total_sum%2==0)
    sort(array.begin(),array.end(),greater<int>());
    else
    sort(array.begin(),array.end());
    return array;
}



