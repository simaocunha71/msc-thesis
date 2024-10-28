    vector<int> all_numbers;
    int current_number=n;
    while (current_number!=1)
    {
        if (current_number%2==1)
        {
            all_numbers.push_back(current_number);
        }
        current_number=(current_number%2==0)?current_number/2:(current_number*3)+1;
    }
    all_numbers.push_back(current_number);
    sort(all_numbers.begin(), all_numbers.end());
    return all_numbers;
}



