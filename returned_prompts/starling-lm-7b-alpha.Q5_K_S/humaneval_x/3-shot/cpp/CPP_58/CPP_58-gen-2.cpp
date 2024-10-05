    vector<int> all_numbers;
    vector<int> common_numbers;
    int i;
    all_numbers.insert(all_numbers.end(),l1.begin(),l1.end());
    all_numbers.insert(all_numbers.end(),l2.begin(),l2.end());
    sort(all_numbers.begin(),all_numbers.end());
    for (i=0;i<all_numbers.size();i++)
    if (i+1==all_numbers.size()||all_numbers[i]!=all_numbers[i+1])
    if (binary_search(l1.begin(),l1.end(),all_numbers[i]))
    if (binary_search(l2.begin(),l2.end(),all_numbers[i]))
    common_numbers.push_back(all_numbers[i]);

    return common_numbers;
}



