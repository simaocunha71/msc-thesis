    vector<int> all_digits;
    int i;
    for (i=0;i<x.size();i++)
    {
        int number=x[i];
        int digit;
        while (number>0)
        {
            digit=number%10;
            if (digit%2!=0)
            all_digits.push_back(digit);
            number/=10;
        }
    }
    sort(all_digits.begin(),all_digits.end());
    return all_digits;
}


