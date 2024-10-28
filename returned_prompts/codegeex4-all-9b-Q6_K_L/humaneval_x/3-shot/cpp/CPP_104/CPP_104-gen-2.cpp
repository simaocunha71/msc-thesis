    vector<int> all_digits;
    int i,j;
    int digit;
    for (i=0;i<x.size();i++)
    {
        int num=x[i];
        bool is_even=true;
        while (num>0)
        {
            digit=num%10;
            if (digit%2==0)
            {
                is_even=false;
                break;
            }
            num=num/10;
        }
        if (is_even)
        {
            all_digits.push_back(x[i]);
        }
    }
    sort(all_digits.begin(), all_digits.end());
    return all_digits;
}

