    int i,j;
    vector<int> array_copy=array;
    int sum=array_copy[0]+array_copy[array_copy.size()-1];
    if (sum%2==0)
    sort(array_copy.begin(), array_copy.end());
    else
    sort(array_copy.begin(), array_copy.end(), greater<int>());
    return array_copy;
}

