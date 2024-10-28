    vector<int> all_numbers;
    if (a%2==0)
    all_numbers.push_back(a);
    if (b%2==0)
    all_numbers.push_back(b);

    for (int i=a+1;i<b;i++)
    if (i%2==0)
    all_numbers.push_back(i);
    return all_numbers;
}


