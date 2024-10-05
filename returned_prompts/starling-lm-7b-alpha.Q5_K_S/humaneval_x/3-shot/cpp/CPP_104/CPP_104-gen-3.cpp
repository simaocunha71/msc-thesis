    vector<int> all_numbers;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        int curr_number=x[i];
        bool is_good=true;
        for (j=1;j<=curr_number;j*=10)
        {
            int digit=curr_number%j;
            if (digit%2==0)
            {
                is_good=false;
                break;
            }
        }
        if (is_good)
        all_numbers.push_back(curr_number);
    }
    sort(all_numbers.begin(), all_numbers.end());
    return all_numbers;
}



