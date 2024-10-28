    vector<int> new_vec;
    int i,j;
    for (i=0;i<numbers.size();i++)
    {
        new_vec.push_back(numbers[i]);
        if (i<numbers.size()-1)
        new_vec.push_back(delimeter);
    }
    return new_vec;
}


