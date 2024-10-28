    vector<int> collatz_odd_numbers;
    vector<int> collatz_numbers;
    int next_number;
    int i;
    collatz_odd_numbers.push_back(n);
    if (n%2==0)
    {
        next_number=n/2;
    }
    if (n%2!=0)
    {
        next_number=n*3+1;
    }
    collatz_numbers.push_back(next_number);
    for (i=0;i<collatz_numbers.size();i++)
    {
        if (collatz_numbers[i]%2==0)
        {
            next_number=collatz_numbers[i]/2;
        }
        if (collatz_numbers[i]%2!=0)
        {
            next_number=collatz_numbers[i]*3+1;
        }
        if (collatz_odd_numbers.size()==0 || collatz_odd_numbers[collatz_odd_numbers.size()-1]<next_number)
        {
            collatz_odd_numbers.push_back(next_number);
            collatz_numbers.push_back(next_number);
        }
    }
    sort(collatz_odd_numbers.begin(),collatz_odd_numbers.end());
    return collatz_odd_numbers;
}


