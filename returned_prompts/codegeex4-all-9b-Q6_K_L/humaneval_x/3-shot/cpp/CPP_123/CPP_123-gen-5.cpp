    vector<int> odd_numbers;
    vector<int> collatz_numbers;
    int i;
    int current_number;
    if (n==1)
    {
        odd_numbers.push_back(1);
        return odd_numbers;
    }
    for (i=1;i<=n;i++)
    collatz_numbers.push_back(i);
    current_number=collatz_numbers[0];
    while (current_number!=1)
    {
        if (current_number%2==1)
        odd_numbers.push_back(current_number);
        if (current_number%2==0)
        current_number=current_number/2;
        else
        current_number=3*current_number+1;
        collatz_numbers.push_back(current_number);
    }
    sort(odd_numbers.begin(),odd_numbers.end());
    return odd_numbers;
}

