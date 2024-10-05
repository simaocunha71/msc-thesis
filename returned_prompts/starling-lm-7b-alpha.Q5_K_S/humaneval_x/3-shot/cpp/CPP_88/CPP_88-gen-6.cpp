    vector<int> new_array=array;
    if (new_array[0]+new_array[new_array.size()-1]%2==0)
    sort(new_array.begin(),new_array.end(),greater<int>());
    else
    sort(new_array.begin(),new_array.end());
    return new_array;
}


