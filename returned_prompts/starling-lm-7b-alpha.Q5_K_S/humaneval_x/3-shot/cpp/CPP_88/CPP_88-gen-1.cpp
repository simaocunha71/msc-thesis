    vector<int> result;
    int i;
    int first_index=0;
    int last_index=(int)array.size()-1;

    if (array[first_index]+array[last_index]%2==0)
    {
    sort(array.begin(), array.end(), greater<int>());
    }
    else
    {
    sort(array.begin(), array.end());
    }

    return array;
}



