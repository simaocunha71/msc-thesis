    sort(numbers.begin(),numbers.end());
    vector<int> temp;
    for (int i=0;i<numbers.size();i++)
    if (i==0)
    temp.push_back(numbers[i]);
    else
    if (numbers[i]!=numbers[i-1])
    temp.push_back(numbers[i]);
    return temp;
}



