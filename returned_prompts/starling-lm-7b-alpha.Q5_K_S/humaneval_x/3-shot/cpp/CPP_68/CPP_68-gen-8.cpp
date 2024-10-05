    int i,j;
    int min_even_value=1000000000;
    int min_even_index=0;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0 && min_even_value>arr[i]){
        min_even_value=arr[i];
        min_even_index=i;
    }
    vector<int> ret_arr;
    if (min_even_value==1000000000)
    return ret_arr;
    else
    {
        ret_arr.push_back(min_even_value);
        ret_arr.push_back(min_even_index);
    }
    return ret_arr;
}



