    vector<int> all_numbers;
    int first_two;
    int current_number;
    int i;
    if (n<2)
    return all_numbers;
    else
    {
    all_numbers.push_back(1);
    all_numbers.push_back(3);
    if (n==2)
    return all_numbers;
    }
    first_two=all_numbers[0]+all_numbers[1];
    all_numbers.push_back(first_two);
    if (n==3)
    return all_numbers;
    for (i=3;i<n+1;i++)
    {
    if (i%2==0)
    current_number=all_numbers[i/2]+all_numbers[(i-1)/2]+all_numbers[(i+1)/2];
    else
    current_number=all_numbers[(i-1)/2]+all_numbers[(i-2)/2]+all_numbers[(i+1)/2];
    all_numbers.push_back(current_number);
    }
    return all_numbers;
}


