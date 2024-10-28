    vector<int> all_numbers;
    vector<int> all_numbers1;
    int i,j;
    for (i=0;i<x.size();i++)
    {
        int num=x[i];
        int flag=0;
        while (num>0)
        {
            int digit=num%10;
            if (digit%2==0)
            {
                flag=1;
                break;
            }
            num=num/10;
        }
        if (flag==0)
        {
            all_numbers.push_back(x[i]);
        }
    }
    sort(all_numbers.begin(),all_numbers.end());
    return all_numbers;
}

