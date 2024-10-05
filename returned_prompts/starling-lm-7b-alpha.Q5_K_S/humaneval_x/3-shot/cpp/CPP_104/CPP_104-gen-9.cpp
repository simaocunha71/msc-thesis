    vector<int> all_numbers;
    int i;
    for (i=0;i<x.size();i++)
    if (num_digits(x[i])%2==1)
    all_numbers.push_back(x[i]);

    sort(all_numbers.begin(),all_numbers.end());
    return all_numbers;
}

