    vector<int> all_digits;
    int i;
    for (i=0;i<x.size();i++)
    all_digits.push_back(x[i]%10);

    sort(all_digits.begin(),all_digits.end());
    vector<int> result;
    int previous=all_digits[0];
    for (i=1;i<all_digits.size();i++)
    if (previous!=all_digits[i])
    result.push_back(previous), previous=all_digits[i];
    result.push_back(previous);
    return result;
}


