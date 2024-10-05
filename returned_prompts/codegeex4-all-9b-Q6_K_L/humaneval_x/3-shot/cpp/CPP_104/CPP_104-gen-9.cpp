    vector<int> all_digits;
    int digit;
    int i,j;
    bool is_even;
    for (i=0;i<x.size();i++)
    {
        digit=x[i];
        is_even=false;
        while (digit>0)
        {
            j=digit%10;
            if (j%2==0)
            {
                is_even=true;
                break;
            }
            digit/=10;
        }
        if (!is_even)
            all_digits.push_back(x[i]);
    }
    sort(all_digits.begin(),all_digits.end());
    return all_digits;
}

