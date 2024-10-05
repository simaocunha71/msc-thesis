    vector<int> all_numbers;
    vector<int> all_numbers_unique;
    int i;
    for (i=0;i<l1.size();i++)
    all_numbers.push_back(l1[i]);
    for (i=0;i<l2.size();i++)
    all_numbers.push_back(l2[i]);
    sort(all_numbers.begin(),all_numbers.end());
    all_numbers_unique.push_back(all_numbers[0]);
    int j;
    for (i=1;i<all_numbers.size();i++)
    {
        if (all_numbers[i]!=all_numbers[i-1])
        {
            all_numbers_unique.push_back(all_numbers[i]);
        }
    }
    vector<int> common_numbers;
    for (i=0;i<all_numbers_unique.size();i++)
    {
        j=0;
        while (j<l1.size() && l1[j]<all_numbers_unique[i])
        j+=1;
        if (j<l1.size() && l1[j]==all_numbers_unique[i])
        {
            while (j<l1.size() && l1[j]==all_numbers_unique[i])
            {
                j+=1;
            }
            if (j<l1.size() && l1[j]==all_numbers_unique[i])
            {
                common_numbers.push_back(all_numbers_unique[i]);
            }
        }
        j=0;
        while (j<l2.size() && l2[j]<all_numbers_unique[i])
        j+=1;
        if (j<l2.size() && l2[j]==all_numbers_unique[i])
        {
            while (j<l2.size() && l2[j]==all_numbers_unique[i])
            {
                j+=