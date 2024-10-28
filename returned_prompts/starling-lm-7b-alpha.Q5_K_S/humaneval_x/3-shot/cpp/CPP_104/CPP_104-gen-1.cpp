    vector<int> all_numbers;
    vector<int> all_numbers_filtered;
    int number,digit;
    int i;
    for (i=0;i<x.size();i++)
    {
        number=x[i];
        all_numbers.push_back(number);
        while(number>0)
        {
            digit=number%10;
            if (digit%2==1)
            {
                all_numbers_filtered.push_back(number);
            }
            number/=10;
        }
    }
    sort(all_numbers_filtered.begin(),all_numbers_filtered.end());
    return all_numbers_filtered;
}



