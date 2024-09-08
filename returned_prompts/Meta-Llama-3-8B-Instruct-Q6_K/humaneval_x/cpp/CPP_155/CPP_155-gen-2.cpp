    vector<int> result;
    int even = 0;
    int odd = 0;
    while(num != 0)
    {
        int digit = num % 10;
        if(digit % 2 == 0)
            even++;
        else
            odd++;
        num /= 10;
    }
    result.push_back(even);
    result.push_back(odd);
    return result;
}

