    vector<int> unique_numbers;
    vector<int>::iterator it;
    for (it=numbers.begin();it<numbers.end();it++)
    {
        int current_number=*it;
        bool exists=false;
        for (int i=0;i<unique_numbers.size();i++)
        {
            if (current_number==unique_numbers[i])
            {
            exists=true;
            break;
            }
        }
        if (!exists)
        {
        unique_numbers.push_back(current_number);
        }
    }
    return unique_numbers;
}



