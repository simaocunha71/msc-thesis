    vector<int> all_numbers;
    int i,j;
    for (i=n;i>0;i-=1)
    {
        if (i%2==0)
        all_numbers.push_back(i/2);
        else
        all_numbers.push_back(3*i+1);
    }
    sort(all_numbers.begin(),all_numbers.end());
    vector<int> odd_numbers;
    for (i=0;i<all_numbers.size();i++)
    if (all_numbers[i]%2==1)
    odd_numbers.push_back(all_numbers[i]);

    return odd_numbers;
}


