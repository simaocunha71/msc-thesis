    vector<int> all_numbers;
    int level=0;
    char chr;
    int i;
    for (i=a;i<=b;i++)
    {
        chr=(char)(i+'0');
        if (chr%2==0)
        all_numbers.push_back(i);
    }
    return all_numbers;
}


